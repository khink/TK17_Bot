"""Storage stuff."""

from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from tk17_tg_bot.result import Result
from tk17_tg_bot.settings import SQL_CONNECTION_STRING

Base = declarative_base()


class VoteCount(Base):
    """Define model for storing votes."""

    __tablename__ = 'votecount'
    id = Column(Integer, primary_key=True)
    chat = Column(Integer)
    option = Column(String)
    count = Column(Integer)

    def __repr__(self):
        """Object representation."""
        return "<VoteCount(chat=%d,option=%s,count=%s)>" % \
            (self.chat, self.option, self.count)


class HasVoted(Base):
    """Define model for storing who has voted."""

    __tablename__ = 'hasvoted'
    id = Column(Integer, primary_key=True)
    chat = Column(Integer)
    user = Column(Integer)

    def __repr__(self):
        """Object representation."""
        return "<HasVoted(chat=%d,user=%s)>" % (self.chat, self.user)


class Storage(object):
    """Storage class."""

    def __init__(self, conn_string=SQL_CONNECTION_STRING, echo=False):
        """Create DB tables if necessary."""
        self.engine = create_engine(conn_string, echo=echo)
        Base.metadata.create_all(self.engine)

    def has_voted(self, user, chat):
        """Return True if user has voted in chat."""
        session = sessionmaker(bind=self.engine)()
        qry = session.query(HasVoted).filter(
            HasVoted.chat.is_(chat),
            HasVoted.user.is_(user))
        if qry.count():
            return True
        new = HasVoted(chat=chat, user=user)
        session.add(new)
        session.commit()
        session.close()
        return False

    def show_votes(self, chat):
        """Show votes for chat."""
        session = sessionmaker(bind=self.engine)()
        votes = {}
        qry = session.query(VoteCount).filter(VoteCount.chat.is_(chat))
        for vote_count in qry.all():
            votes[vote_count.option] = vote_count.count
        session.close()
        return Result(votes).text()

    def store_vote(self, user, chat, vote_option):
        """Store a vote."""
        session = sessionmaker(bind=self.engine)()
        if self.has_voted(user, chat):
            return "Je hebt al gestemd in deze chat."
        qry = session.query(VoteCount).filter(
            VoteCount.chat.is_(chat),
            VoteCount.option.is_(vote_option))
        if qry.count():
            vote_count = qry.first()
            vote_count.count += 1
        else:
            new = VoteCount(chat=chat, option=vote_option, count=1)
            session.add(new)
        session.commit()
        session.close()
        return "Je stem op %s is opgeslagen" % vote_option

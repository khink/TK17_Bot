"""Storage stuff."""

from collections import defaultdict

from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from tk17_tg_bot.result import Result

SQL_CONNECTION_STRING = 'sqlite:///tk17tgbot.db'
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


class Storage(object):
    """Storage class."""

    users_voted = defaultdict(dict)

    def __init__(self, conn_string=SQL_CONNECTION_STRING, echo=False):
        """Create DB tables if necessary."""
        self.engine = create_engine(conn_string, echo=echo)
        Base.metadata.create_all(self.engine)

    def get_session(self):
        """Create or return session."""
        if not hasattr(self, '_session'):
            self._session = sessionmaker(bind=self.engine)()
        return self._session

    def has_voted(self, user, chat):
        """Return True if user has voted in chat."""
        if user in self.users_voted[chat]:
            return True
        self.users_voted[chat][user] = True
        return False

    def show_votes(self, chat):
        """Show votes for chat."""
        session = self.get_session()
        votes = {}
        qry = session.query(VoteCount).filter(VoteCount.chat.is_(chat))
        for vote_count in qry.all():
            votes[vote_count.option] = vote_count.count
        return Result(votes).text()

    def store_vote(self, user, chat, vote_option):
        """Store a vote."""
        session = self.get_session()
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
        return "Je stem op %s is opgeslagen" % vote_option

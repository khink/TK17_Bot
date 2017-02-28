"""Storage stuff."""

from collections import defaultdict

from tk17_tg_bot.result import Result


class Storage(object):
    """Storage class."""

    votes = defaultdict(dict)
    users_voted = defaultdict(dict)

    def has_voted(self, user, chat):
        """Return True if user has voted in chat."""
        if user in self.users_voted[chat]:
            return True
        self.users_voted[chat][user] = True
        return False

    def show_votes(self, chat):
        """Show votes for chat."""
        return Result(self.votes[chat]).text()

    def store_vote(self, user, chat, vote_option):
        """Store a vote."""
        if self.has_voted(user, chat):
            return "Je hebt al gestemd in deze chat."
        if vote_option in self.votes[chat]:
            self.votes[chat][vote_option] += 1
        else:
            self.votes[chat][vote_option] = 1
        return "Je stem op %s is opgeslagen" % vote_option

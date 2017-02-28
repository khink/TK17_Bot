"""Result formatting."""


class Result(object):
    """Class for formatting raw votes data."""

    def __init__(self, votes):
        """Store votes."""
        # raw votes
        self.votes = votes
        # list of options in decreasing popularity
        self.options = sorted(votes, key=self.votes.get, reverse=True)

    def text(self):
        """Render as string."""
        if not self.votes:
            return "Er is nog niet gestemd."
        return '\n'.join(["%s: %s" % (key, self.votes[key])
                          for key in self.options])

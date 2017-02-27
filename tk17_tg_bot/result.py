"""Result formatting."""


class Result(object):
    """Class for formatting raw votes data."""

    def __init__(self, votes):
        """Store raw votes."""
        self.votes = votes

    def __str__(self):
        """Render as string."""
        if not self.votes:
            return "Er is nog niet gestemd."
        return '\n'.join(["%s: %s" % (key, self.votes[key])
                          for key in sorted(self.votes,
                                            key=self.votes.get,
                                            reverse=True)])

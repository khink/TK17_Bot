"""Result formatting."""


class Result(object):
    """Class for formatting raw votes data."""

    def __init__(self, votes):
        """Store raw votes by popularity."""
        self.votes = sorted(votes,
                            key=self.votes.get,
                            reverse=True)

    def __str__(self):
        """Render as string."""
        return '\n'.join(
            ["%s: %s" % (key, value)
             for key, value in self.sorted_votes.iteritems()])

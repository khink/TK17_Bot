"""Test formatting of results."""

import json

from tk17_tg_bot.constants import VOTING_OPTIONS
from tk17_tg_bot.markup import markup_options


def test_voting_options():
    assert VOTING_OPTIONS[-2:] == ['blanco', 'niet']


def test_keyboard_rows():
    """Test that all options show in keyboard."""
    markup = markup_options()
    keyboard = json.loads(markup.to_json())['keyboard']
    assert keyboard[-1] == [{u'text': u'/stem blanco'},
                            {u'text': u'/stem niet'}]

"""Test formatting of results."""

from tk17_tg_bot.result import Result

raw_result = {
    'aap': 2,
    'noot': 3,
    'mies': 1,
}


def test_order():
    """Test that results option are reverse-sorted on popularity."""
    result = Result(raw_result)
    assert str(result) == """noot: 3\naap: 2\nmies: 1"""

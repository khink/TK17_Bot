"""Test formatting of results."""

from tk17_tg_bot.storage import Storage


def test_storage():
    """Test that storage works.

    Allow 1 vote per user per chat.
    """
    user_1_id = 500
    chat_1_id = 1000
    storage = Storage()
    # cast vote
    result = storage.store_vote(user_1_id, chat_1_id, 'henk')
    # test voting feedback
    assert result == "Je stem op henk is opgeslagen"
    # new vote is stored
    assert storage.show_votes(chat_1_id) == 'henk: 1'
    # user can't vote again
    assert storage.has_voted(user_1_id, chat_1_id) is True
    result = storage.store_vote(user_1_id, chat_1_id, 'henk')
    # test voting feedback
    assert result == "Je hebt al gestemd in deze chat."
    assert storage.show_votes(chat_1_id) == 'henk: 1'

    # Another user votes.
    user_2_id = 501
    # cast vote
    result = storage.store_vote(user_2_id, chat_1_id, 'jos')
    # test voting feedback
    assert result == "Je stem op jos is opgeslagen"
    # new vote is stored
    assert 'jos: 1' in storage.show_votes(chat_1_id)
    # user can't vote again
    assert storage.has_voted(user_2_id, chat_1_id) is True
    result = storage.store_vote(user_2_id, chat_1_id, 'henk')
    # test voting feedback
    assert result == "Je hebt al gestemd in deze chat."
    assert 'jos: 1' in storage.show_votes(chat_1_id)

    # Users can still vote in another chat.
    chat_2_id = 1001
    # cast vote
    result = storage.store_vote(user_1_id, chat_2_id, 'henk')
    # test voting feedback
    assert result == "Je stem op henk is opgeslagen"
    # new vote is stored
    assert storage.show_votes(chat_2_id) == 'henk: 1'
    # user can't vote again
    assert storage.has_voted(user_1_id, chat_2_id) is True
    result = storage.store_vote(user_1_id, chat_2_id, 'henk')
    # test voting feedback
    assert result == "Je hebt al gestemd in deze chat."
    assert storage.show_votes(chat_2_id) == 'henk: 1'

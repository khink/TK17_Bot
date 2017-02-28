"""Markup stuff."""

from telebot import types

from tk17_tg_bot.constants import COMMAND_VOTE, VOTING_OPTIONS

COLS = 2  # nr of columns in markup


def markup_options():
    """Return options marked up for easy clicky-clicky."""
    markup = types.ReplyKeyboardMarkup(row_width=COLS)
    for row_idx in range(len(VOTING_OPTIONS) / COLS):
        opt_idx = row_idx * COLS
        buttons = []
        while opt_idx < (row_idx + 1) * COLS:
            # create a button that submits a vote
            msg = "/%s %s" % (COMMAND_VOTE, VOTING_OPTIONS[opt_idx])
            buttons.append(types.KeyboardButton(msg))
            opt_idx += 1
            if opt_idx >= len(VOTING_OPTIONS):
                # not enough options to put COLS options in last row
                break
        markup.row(*buttons)
    return markup

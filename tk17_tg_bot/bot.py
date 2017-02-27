"""Main program loop and message handlers."""

import logging

from telebot import logger

from tk17_tg_bot.keys import TOKEN
from tk17_tg_bot.markup import markup_options
from tk17_tg_bot.storage import TK17TgBot
from tk17_tg_bot.constants import (
    COMMAND_OPTIONS,
    COMMAND_RESULT,
    COMMAND_VOTE,
    VOTING_OPTIONS,
)

logger = logger
logger.setLevel(logging.DEBUG)


def _help_vote(msg=''):
    """Help for the vote command."""
    msg += "Geldige opties zijn:\n"
    msg += "\n".join(VOTING_OPTIONS)
    return msg

bot = TK17TgBot(TOKEN)


@bot.message_handler(commands=[COMMAND_VOTE])
def handle_vote(message):
    """Handle a vote."""
    try:
        vote_option = message.text.split(COMMAND_VOTE)[1].strip()
    except IndexError:
        # empty vote
        bot.reply_to(message, _help_vote("Waarop wil je stemmen? "))
        return
    if vote_option.lower() in ['hitler', 'putin', 'trump']:
        bot.reply_to(message,
                     "That option is not available, but PVV is close. ")
    if vote_option not in VOTING_OPTIONS:
        # invalid choice
        bot.reply_to(message, _help_vote("Kies een geldige stemoptie. "))
        return
    bot.reply_to(
        message,
        bot.store_vote(message.from_user.id, message.chat.id, vote_option),
    )


@bot.message_handler(commands=[COMMAND_RESULT])
def result(message):
    """Show result."""
    bot.reply_to(message, bot.show_votes(message.chat.id))


@bot.message_handler(commands=[COMMAND_OPTIONS])
def options(message):
    """Show options."""
    bot.send_message(message.chat.id,
                     "Maak een keuze:",
                     reply_markup=markup_options())

bot.polling()

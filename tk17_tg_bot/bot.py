"""Main program loop and message handlers."""

import logging

from telebot import TeleBot, logger

from tk17_tg_bot.markup import markup_options
from tk17_tg_bot.settings import TOKEN
from tk17_tg_bot.storage import Storage
from tk17_tg_bot.constants import (
    COMMAND_OPTIONS,
    COMMAND_RESULT,
    COMMAND_VOTE,
    VOTING_OPTIONS,
)

logger = logger
logger.setLevel(logging.INFO)

bot = TeleBot(TOKEN)
storage = Storage()


@bot.message_handler(commands=['start', 'help'])
def send_welcome_message(message):
    """Welcome message and help."""
    bot.send_message(
        message.chat.id, """
        Voeg deze bot toe aan uw kanaal om een poll te starten.

        Commando's:
        /opties - Laat knoppen met mogelijke keuzes zien
        /stem - Kies een partij (of stem blanco, of niet)
        /uitslag - Laat tussenstand zien
"""
    )


@bot.message_handler(commands=[COMMAND_VOTE])
def handle_vote(message):
    """Handle a vote."""
    try:
        vote_option = message.text.split(COMMAND_VOTE)[1].strip()
    except IndexError:
        # empty vote
        bot.reply_to(message, "Maak een keuze:",
                     reply_markup=markup_options())
        return
    if vote_option.lower() in ['orban', 'duterte', 'putin', 'trump']:
        bot.reply_to(message, "Die hebben we niet, maar probeer de PVV eens. ")
        return
    if vote_option not in VOTING_OPTIONS:
        # invalid choice
        bot.reply_to(message, "Maak een keuze:",
                     reply_markup=markup_options())
        return
    bot.reply_to(
        message,
        storage.store_vote(message.from_user.id, message.chat.id, vote_option),
    )


@bot.message_handler(commands=[COMMAND_RESULT])
def result(message):
    """Show result."""
    bot.reply_to(message, storage.show_votes(message.chat.id))


@bot.message_handler(commands=[COMMAND_OPTIONS])
def options(message):
    """Show options."""
    bot.send_message(message.chat.id,
                     "Maak een keuze:",
                     reply_markup=markup_options())

bot.polling()

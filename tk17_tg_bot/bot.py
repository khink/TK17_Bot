"""Main program loop and message handlers."""

import logging
import telebot
from collections import defaultdict

from tk17_tg_bot.keys import TOKEN
from tk17_tg_bot.parties import VOTING_OPTIONS
from tk17_tg_bot.result import Result

RESULT_COMMAND = 'uitslag'
VOTE_COMMAND = 'stem'
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)


def _help_vote(msg=''):
    """Help for the vote command."""
    msg += "Geldige opties zijn:\n"
    msg += "\n".join(VOTING_OPTIONS)
    return msg


class TK17TgBot(telebot.TeleBot):
    """Subclass telebot for votes storage."""

    votes = defaultdict(dict)
    users_voted = defaultdict(dict)

    def has_voted(self, user, chat):
        """Return True if user has voted in chat."""
        if user in self.users_voted[chat]:
            return True
        self.users_voted[chat][user] = True

    def show_votes(self, chat):
        """Show votes for chat."""
        return Result(self.votes[chat])

    def store_vote(self, user, chat, vote_option):
        """Store a vote."""
        if self.has_voted(user, chat):
            return "Je hebt al gestemd in deze chat."
        if vote_option in self.votes[chat]:
            self.votes[chat][vote_option] += 1
        else:
            self.votes[chat][vote_option] = 1
        return "Je stem op %s is opgeslagen" % vote_option


def main():
    """Main loop."""
    bot = TK17TgBot(TOKEN)

    @bot.message_handler(commands=[VOTE_COMMAND])
    def handle_vote(message):
        """Handle a vote."""
        try:
            vote_option = message.text.split(VOTE_COMMAND)[1].strip()
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

    @bot.message_handler(commands=[RESULT_COMMAND])
    def result(message):
        """Show result."""
        bot.reply_to(message, bot.show_votes(message.chat.id))

    bot.polling()

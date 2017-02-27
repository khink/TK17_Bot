# Tweede kamerverkiezingen Telegram Bot

This is Telegram bot to add a poll for the 2017 Dutch parliament elections.

## Usage

To use it in Telegram, search for the user `TK17_Bot` and add it to a chat.


###  Commands

- `/stem {OPTION}` casts a vote (shows list of options if empty)
- `/uitslag` shows results


### Voting options

The list of available options will be shown when you cast an empty vote.

Note that this is case-sensitive.

There's also options for:
- blanco ("I will go voting but i'll leave it empty")
- niet ("I will stay at home and play Rocket League")


## About

This bot was programmed in Python using pyTelegramBotAPI.


## How to install

  virtualenv .
  . bin/activate
  python setup.py install


## Configure

Place the Telegram Bot API token in `tk17_tg_bot/keys.py` as in
`keys.py.example`:

  TOKEN = ''


## How to run

  ./bin/run_bot


## Storage

Storage is volatile, when you quit the `run_bot` command all results are lost.


## Privacy

To ensure one vote per account per chat, the combination of user_id + chat_id
is marked as used when a user has voted in a chat.

We don't store what option a user voted for.
This might be relevant for privacy if we would use a persistent database.

This bot doesn't listen to any other messages from the chat, just the commands
listed above.


## Development

Pull requests are welcome!

# Tweede kamerverkiezingen Telegram Bot

This is a Telegram bot to add a poll for the 2017 Dutch parliament elections.


## About TK17_Bot

To use this bot in Telegram, search for the user `TK17_Bot` and add it to a chat.


###  Commands

- `/stem {OPTION}` casts a vote (shows list of options if empty)
- `/uitslag` shows results
- `/opties` shows the list of options


### Voting options

The list of available options will be shown when you cast an empty vote.
(Note that the voting options are case-sensitive, remember this when you type
instead of clicking one of the buttons that the bot provides.)

There's also options for:
- blanco ("I will go voting but i'll leave it empty")
- niet ("I will stay at home and play Rocket League")

There's no option for "undecided", because in the end you would end up choosing
one of the other options.
Just like in some types of political debate, there is no room for nuance here :)
"Invalid" is left out intentionally, assuming no one does that on purpose.


## About the software

This bot was programmed in Python using
[pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI#).


### How to install

```
virtualenv .
. bin/activate
python setup.py install
```


### Configure

Place the [Telegram Bot API token](https://core.telegram.org/bots)
in `tk17_tg_bot/settings.py` as in `settings.py.example`:

`TOKEN = ''`

Using Botfather, add an image to the bot, and edit the commands:

```
stem - Kies een partij (of stem blanco, of niet)
uitslag - Laat tussenstand zien
opties - Laat mogelijke keuzes zien
help - Laat dit scherm zien
```

### How to run

`python -m tk17_tg_bot.bot`


### Storage

SQLAlchemy is used to store data. The easiest way to make this work is to edit
`settings.py` and set `SQL_CONNECTION_STRING = 'sqlite:///database.db'`.
This will store the file in your project directory.


### Privacy

To ensure one vote per account per chat, the combination of user_id + chat_id
is marked as used when a user has voted in a chat.

We don't store what option a user voted for.

This bot doesn't listen to any other messages from the chat, just the commands
listed above.


### Development

Pull requests are welcome!


### Tests

Using [pytest](http://doc.pytest.org/en/latest/). Run:

`pytest tk17_tg_bot`


### Roadmap

- Run as server process
- Logging
- Confidential voting (don't show channel what you voted)
- Nicer result rendering (pie chart, percentage, number of seats)
- Enable closing the poll


### Compatibility

Tried on Python2.7 and Python3.4.


### License

GPLv3.

See https://www.gnu.org/licenses/gpl-3.0.txt or the LICENSE.txt.

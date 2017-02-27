# Tweede kamerverkiezingen Telegram Bot

This is Telegram bot to add a poll for the 2017 Dutch parliament elections.


## About TK17_Bot

To use this bot in Telegram, search for the user `TK17_Bot` and add it to a chat.


###  Commands

- `/stem {OPTION}` casts a vote (shows list of options if empty)
- `/uitslag` shows results
- `/opties` shows the list of options


### Voting options

The list of available options will be shown when you cast an empty vote.

Note that this is case-sensitive.

There's also options for:
- blanco ("I will go voting but i'll leave it empty")
- niet ("I will stay at home and play Rocket League")

There's no option for "undecided", because in the end you would end up choosing
one of the other options.
Just like in some types of political debate, there is no room for nuance here :)


## About the software

This bot was programmed in Python using pyTelegramBotAPI.


### How to install

```
virtualenv .
. bin/activate
python setup.py install
```


### Configure

Place the Telegram Bot API token in `tk17_tg_bot/keys.py` as in
`keys.py.example`:

`TOKEN = ''`

Using Botfather, add an image to the bot, and edit the commands:

```
stem - Kies een partij (of stem blanco, of niet)
uitslag - Laat tussenstand zien
opties - Laat mogelijke keuzes zien
```

### How to run

`python -m tk17_tg_bot.bot`


### Storage

Storage is volatile, when you quit the Python command all results are lost.


### Privacy

To ensure one vote per account per chat, the combination of user_id + chat_id
is marked as used when a user has voted in a chat.

We don't store what option a user voted for.
This might be relevant for privacy if we would use a persistent database.

This bot doesn't listen to any other messages from the chat, just the commands
listed above.


### Development

Pull requests are welcome!

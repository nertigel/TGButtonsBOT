# TGButtonsBOT for Telegram
This is a telegram bot based off the [Pyrogram](https://github.com/pyrogram/pyrogram) library in Python3. 

# How it works

The bot will automatically attach pre-defined buttons to messages that are sent in your channel/group as long as the bot has permission to do so.
Thought of selling it but ts garbage fr.

# Installation

You can run this bot on your own, install the required lib by running this command: 

```bash
pip install pyrogram
```


In the `data.json` file you will find api_id, api_hash and bot_token variables, get your [API credentials from Telegram's official website](https://my.telegram.org/auth) and bot's token from the [BotFather](https://telegram.me/botfather) and replace `YOUR_TOKEN_HERE` with your token:

`data.json`:
```json
{
    "api_id": "",
    "api_hash": "",
    "bot_token": "YOUR_TOKEN_HERE",
    "admin_user_id": "630271827",
    "buttons": [
        ["לרכישה", "https://t.me/nertigel"],
        ["ערוץ ביקורות", "https://t.me/nertigels"]
    ]
}
```

Now you can simply run the bot by running `main.py`

Make sure the bot has permissions to send/edit messages!

import json
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Load configuration from JSON file
with open('data.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

api_id = config["api_id"]
api_hash = config["api_hash"]
bot_token = config["bot_token"]
admin_user_id = int(config["admin_user_id"])  # Make sure the user ID is an integer

# Initialize the client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

def create_keyboard(buttons):
    return InlineKeyboardMarkup([
        #[InlineKeyboardButton(text, url=url) for text, url in buttons] # horizontal
        [InlineKeyboardButton(text, url=url)] for text, url in buttons # vertical
    ])

# Load buttons from config
keyboard = create_keyboard(config["buttons"])

async def add_buttons_to_message(client, message):
    try:
        if message.text:
            await client.edit_message_text(
                chat_id=message.chat.id,
                message_id=message.id,
                text=message.text,
                reply_markup=keyboard
            )
        elif message.photo or message.video:
            await client.edit_message_caption(
                chat_id=message.chat.id,
                message_id=message.id,
                caption=message.caption if message.caption else "",
                reply_markup=keyboard
            )
        else:
            print("Message type not supported for editing.")
    except Exception as e:
        print(f"Error editing message: {e}")

@app.on_message(filters.channel & filters.incoming)
async def add_buttons(client, message):
    await add_buttons_to_message(client, message)

@app.on_edited_message(filters.channel)
async def reapply_buttons(client, message):
    await add_buttons_to_message(client, message)

@app.on_message(filters.private & filters.user(admin_user_id))
async def update_buttons(client, message):
    try:
        new_buttons = []
        for line in message.text.split('\n'):
            parts = line.split(' - ')
            if len(parts) == 2:
                new_buttons.append((parts[0].strip(), parts[1].strip()))

        if new_buttons:
            global keyboard
            keyboard = create_keyboard(new_buttons)

            # Update the JSON file
            config["buttons"] = new_buttons
            with open('data.json', 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=4)
            
            await message.reply("Buttons updated successfully!")
        else:
            await message.reply("Invalid input format. Please use the correct format.")
    except Exception as e:
        await message.reply(f"Error updating buttons: {e}")

#@app.on_callback_query()
#async def handle_callback_query(client, callback_query):
#    await callback_query.answer("Button clicked!")

if __name__ == "__main__":
    try:
        print("Building Application...")
        app.run()
    except KeyboardInterrupt:
        print("KeyboardInterrupted by user (Ctrl+C)")

    print("Bot has been stopped!")
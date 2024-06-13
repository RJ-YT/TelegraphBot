import os
from plugins.config import Config
from pyrogram import Client, filters

# Create a Pyrogram Client
app = Client(
    "my_bot",
    api_id=Config.API_ID, 
    api_hash=Config.API_HASH, 
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins")
)

# Start The Bot
print("🗿 I AM ALIVE × @Telegraph-Bot")
app.run()

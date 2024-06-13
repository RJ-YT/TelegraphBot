from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from pyrogram import Client, filters
from pyrogram.types import Message



# Define handlers for different types of messages
@Client.on_message(filters.sticker)
async def handle_sticker(bot, message: Message):
    # Handle sticker message
    await message.reply_text(f"**Sticker File ID:**\n\n `{message.sticker.file_id}`")
  
@Client.on_message(filters.document)
async def handle_document(bot, message: Message):
    # Handle document message
    await message.reply_text(f"**Document File ID:**\n\n `{message.document.file_id}`")

# Define handlers for voice and audio messages
@Client.on_message(filters.voice)
async def handle_voice(bot, message: Message):
    # Handle voice message
    await message.reply_text(f"**Voice File ID:**\n\n `{message.voice.file_id}`")

@Client.on_message(filters.audio)
async def handle_audio(bot, message: Message):
    # Handle audio message
    await message.reply_text(f"**Audio File ID:**\n\n `{message.audio.file_id}`")
    

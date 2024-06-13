import pyrogram, asyncio, random, time, os
import time
import psutil
import shutil
import string
import asyncio
from pyrogram import Client, filters, enums
from asyncio import TimeoutError
from pyrogram.errors import MessageNotModified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, ForceReply
from plugins.config import Config
from plugins.script import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["start"]) & filters.private)
async def start(bot, update): 
    await update.reply_text(
        text=Translation.START_TEXT.format(update.from_user.mention),
        reply_markup=Translation.BOTCHANNEL_BUTTON
    )
    
@Client.on_message(filters.command(["help"]) & filters.private)
async def help(bot, update): 
    await update.reply_text(
        text=Translation.HELP_TEXT
    )

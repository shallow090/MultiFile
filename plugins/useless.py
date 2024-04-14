from bot import Bot1,Bot2
from pyrogram.types import Message
from pyrogram import filters
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT
from datetime import datetime
from helper_func import get_readable_time

@Bot1.on_message(filters.command('stats') & filters.user(ADMINS))
@Bot2.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot: Bot1,Bot2, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=time))


@Bot1.on_message(filters.private & filters.incoming)
@Bot2.on_message(filters.private & filters.incoming)
async def useless(_,message: Message):
    if USER_REPLY_TEXT:
        await message.reply(USER_REPLY_TEXT)

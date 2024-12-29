import os, asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

bot = Client(
    "Remove FwdTag",
    bot_token = "Paste Your Actual Bot Token Here",  # Hardcoded bot token
    api_id = Paste Your API ID,   # Hardcoded API ID
    api_hash = "Then API Hash"  # Hardcoded API hash
)


START_TXT = """
Hi {}, I'm Forward Tag Remover Bot Developed By @abirxdhackz.\n\nForward me some messages, I will remove the forward tag from them.\nI can also do this in channels.
"""

START_BTN = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton('Dev Channel', url='t.me/abir_xd_bio'),
    ]]
)


@bot.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TXT.format(update.from_user.mention)
    reply_markup = START_BTN
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@bot.on_message(filters.channel & filters.forwarded)
async def fwdrmv(c, m):
    try:
        if m.media and not (m.video_note or m.sticker):
            await m.copy(m.chat.id, caption = m.caption if m.caption else None)
            await m.delete()
        else:
            await m.copy(m.chat.id)
            await m.delete()
    except FloodWait as e:
        await asyncio.sleep(e.value)


@bot.on_message(filters.private | filters.group)
async def fwdrm(c, m):
    try:
        if m.media and not (m.video_note or m.sticker):
            await m.copy(m.chat.id, caption = m.caption if m.caption else None)
        else:
            await m.copy(m.chat.id)
    except FloodWait as e:
        await asyncio.sleep(e.value)


bot.run()

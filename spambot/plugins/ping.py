from spambot import *
from spambot import MafiaBot1, MafiaBot2, MafiaBot3, MafiaBot4, MafiaBot5
from telethon.sync import events
from datetime import datetime

@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/ping'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/ping'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/ping'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/ping'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/ping'))
async def ping(e):
    if e.sender_id in MY_USERS:
        before = datetime.now()
        message = await e.client.send_message(e.chat_id, "`Pinging.....!`")
        after = datetime.now()
        ms = (after - before).microseconds / 1000
        await e.client.edit_message(message, f"Ping Pong!\n\nMafia Spam Bot\n\nMy Master:- [{OWNER_NAME}](tg://user?id={OWNER_ID})\n\nPing:- {ms} ms\n\nMafia Spam Bot On Fire")

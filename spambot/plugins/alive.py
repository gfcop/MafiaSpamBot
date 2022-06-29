from spambot import *
from spambot import MafiaBot1, MafiaBot2, MafiaBot3, MafiaBot4, MafiaBot5
from telethon.sync import events
from telethon import version


master = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"


alive_msg = f"""
Mafia Spam Bot Is Alive!

My Master:- {master}

Bot Version:- `{BOT_VERSION}`

Telethon Version:- `{version.__version__}`

{BIO_MSG}
"""

@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/alive'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/alive'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/alive'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/alive'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/alive'))
async def alive(e):
    if e.sender_id in MY_USERS:
        try:
            await e.client.send_file(e.chat_id, DISPLAY_PIC, caption=alive_msg)
        except Exception as e:
            print(e)

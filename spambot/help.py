from spambot import *
from spambot import MafiaBot1, MafiaBot2, MafiaBot3, MafiaBot4, MafiaBot5
from spambot.helpers.commands import *
from telethon import events, Button


Buttons = [
    Button.inline("Alive", b'alive'),
    Button.inline("Ping", b'ping')
], [
    Button.inline("Raid", b'raid'),
    Button.inline("Reply Raid", b'replyraid')
], [
    Button.inline("Spam", b'spam'),
    Button.inline("Pspam", b'pspam')
], [
    Button.inline("Extras", b'extras')
], [
    Button.url("Channel", "t.me/MafiaBot_Support"),
    Button.url("Group", "t.me/MafiaBot_ChitChat")
]

BACK = [
    Button.inline("Back", b'back')
]

@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/help'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/help'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/help'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/help'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/help'))
async def help(e):
    if e.sender_id in MY_USERS:
        message = await e.client.send_file(e.chat_id, DISPLAY_PIC, caption="This Is Help Command!!!", buttons=Buttons)

        


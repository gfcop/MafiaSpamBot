from spambot import *
from spambot.help import *
from spambot.helpers.commands import *
from telethon.sync import events


@MafiaBot1.on(events.CallbackQuery(data=b'alive'))
@MafiaBot2.on(events.CallbackQuery(data=b'alive'))
@MafiaBot3.on(events.CallbackQuery(data=b'alive'))
@MafiaBot4.on(events.CallbackQuery(data=b'alive'))
@MafiaBot5.on(events.CallbackQuery(data=b'alive'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{ALIVE_CMD}", buttons=BACK)

@MafiaBot1.on(events.CallbackQuery(data=b'ping'))
@MafiaBot2.on(events.CallbackQuery(data=b'ping'))
@MafiaBot3.on(events.CallbackQuery(data=b'ping'))
@MafiaBot4.on(events.CallbackQuery(data=b'ping'))
@MafiaBot5.on(events.CallbackQuery(data=b'ping'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{PING_CMD}", buttons=BACK)

@MafiaBot1.on(events.CallbackQuery(data=b'raid'))
@MafiaBot2.on(events.CallbackQuery(data=b'raid'))
@MafiaBot3.on(events.CallbackQuery(data=b'raid'))
@MafiaBot4.on(events.CallbackQuery(data=b'raid'))
@MafiaBot5.on(events.CallbackQuery(data=b'raid'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{RAID_CMD}", buttons=BACK)

@MafiaBot1.on(events.CallbackQuery(data=b'replyraid'))
@MafiaBot2.on(events.CallbackQuery(data=b'replyraid'))
@MafiaBot3.on(events.CallbackQuery(data=b'replyraid'))
@MafiaBot4.on(events.CallbackQuery(data=b'replyraid'))
@MafiaBot5.on(events.CallbackQuery(data=b'replyraid'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{REPLYRAID_CMD}", buttons=BACK)

@MafiaBot1.on(events.CallbackQuery(data=b'spam'))
@MafiaBot2.on(events.CallbackQuery(data=b'spam'))
@MafiaBot3.on(events.CallbackQuery(data=b'spam'))
@MafiaBot4.on(events.CallbackQuery(data=b'spam'))
@MafiaBot5.on(events.CallbackQuery(data=b'spam'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{SPAM_CMD}", buttons=BACK)

@MafiaBot1.on(events.CallbackQuery(data=b'pspam'))
@MafiaBot2.on(events.CallbackQuery(data=b'pspam'))
@MafiaBot3.on(events.CallbackQuery(data=b'pspam'))
@MafiaBot4.on(events.CallbackQuery(data=b'pspam'))
@MafiaBot5.on(events.CallbackQuery(data=b'pspam'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{PSPAM_CMD}", buttons=BACK)

@MafiaBot1.on(events.CallbackQuery(data=b'extras'))
@MafiaBot2.on(events.CallbackQuery(data=b'extras'))
@MafiaBot3.on(events.CallbackQuery(data=b'extras'))
@MafiaBot4.on(events.CallbackQuery(data=b'extras'))
@MafiaBot5.on(events.CallbackQuery(data=b'extras'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{EXTRA_CMD}", buttons=BACK)

@MafiaBot1.on(events.CallbackQuery(data=b'back'))
@MafiaBot2.on(events.CallbackQuery(data=b'back'))
@MafiaBot3.on(events.CallbackQuery(data=b'back'))
@MafiaBot4.on(events.CallbackQuery(data=b'back'))
@MafiaBot5.on(events.CallbackQuery(data=b'back'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit("This Is Help Command!!!", buttons=Buttons)
 
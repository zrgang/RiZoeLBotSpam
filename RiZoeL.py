import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RRAID


a = API_ID
b = API_HASH
smex = STRING
smexx = STRING2
smexxx = STRING3
smexxxx = STRING4
smexxxxx = STRING5


idk = ""
ydk = ""
wdk = ""
sdk = ""
hdk = ""


que = {}

SMEX_USERS = []
for x in SUDO:
    SMEX_USERS.append(x)
    
async def start_rizoel():
    global idk
    global ydk
    global wdk
    global sdk
    global hdk
    if smex:
        session_name = str(smex)
        print("String 1 Found")
        idk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await idk.start()
            botme = await idk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            idk = "smex"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        idk = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception as e:
            pass
   
    if smexx:
        session_name = str(smexx)
        print("String 2 Found")
        ydk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await ydk.start()
            botme = await ydk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "startup"
        ydk = TelegramClient(session_name, a, b)
        try:
            await ydk.start()
        except Exception as e:
            pass

    if smexxx:
        session_name = str(smexxx)
        print("String 3 Found")
        wdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await  wdk.start()
            botme = await wdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "startup"
        wdk = TelegramClient(session_name, a, b)
        try:
            await wdk.start()
        except Exception as e:
            pass

    if smexxxx:
        session_name = str(smexxxx)
        print("String 4 Found")
        hdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await hdk.start()
            botme = await hdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "startup"
        hdk = TelegramClient(session_name, a, b)
        try:
            await hdk.start()
        except Exception as e:
            pass

    if smexxxxx:
        session_name = str(smexxxxx)
        print("String 5 Found")
        sdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await sdk.start()
            botme = await sdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "startup"
        sdk = TelegramClient(session_name, a, b)
        try:
            await sdk.start()
        except Exception as e:
            pass              

loop = asyncio.get_event_loop()
loop.run_until_complete(start_rizoel())       

async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        pass

RIZ_PIC = "https://telegra.ph/file/0c113b325fe639b09a2d5.jpg"
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.bleave"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bleave"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bleave"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bleave"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bleave"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝘽𝙤𝙩 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.bleave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = rizoel[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
                
        
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.bspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝘽𝙤𝙩𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bspam <count> <message to spam>\n\n.bspam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(rizoel) == 2:
            message = str(rizoel[1])
            counter = int(rizoel[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:  
            counter = int(rizoel[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(rizoel[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            

@idk.on(events.NewMessage(incoming=True, pattern=r"\.dspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.dspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.dspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.dspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.dspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.dspam <sleep time> <count> <message to spam>\n\n.dspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        smex = await e.get_reply_message()
        rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        rizoelop = rizoel[1:]
        if len(rizoelop) == 2:
            message = str(rizoelop[1])
            counter = int(rizoelop[0])
            sleeptime = float(rizoel[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(rizoelop[0])
            sleeptime = float(rizoel[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(rizoelop[0])
            sleeptime = float(rizoel[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.bigbspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bigbspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bigbspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bigbspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bigbspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴 𝗕𝗼𝘁 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigbspam <count> <message to spam>\n\n.bigbspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(rizoel) == 2:
            message = str(rizoel[1])
            counter = int(rizoel[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(rizoel[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(rizoel[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.fuk"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.fuk"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.fuk"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.fuk"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.fuk"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗙𝘂𝗸 \n\nCommand:\n\n.fuk <count> <Username of User>\n\n.fuk <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(rizoel) == 2:
            message = str(rizoel[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(rizoel[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(rizoel[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )





@idk.on(events.NewMessage(incoming=True))
@ydk.on(events.NewMessage(incoming=True))
@wdk.on(events.NewMessage(incoming=True))
@hdk.on(events.NewMessage(incoming=True))
@sdk.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )           
            
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.replyfuk"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.replyfuk"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.replyfuk"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.replyfuk"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.replyfuk"))
async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗙𝘂𝗸\n\nCommand:\n\n.replyfuk <Username of User>\n\n.replyfuk <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(rizoel[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyfuk"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyfuk"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyfuk"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyfuk"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyfuk"))
async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗙𝘂𝗸\n\nCommand:\n\n.dreplyfuk <Username of User>\n\n.dreplyfuk <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(rizoel[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
       

@idk.on(events.NewMessage(incoming=True, pattern=r"\.bot"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bot"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bot"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bot"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bot"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "RuKo Jara Sabar Karo..!!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀\n▒█▀▀▄ ▒█░░▒█ ░▒█░░\n▒█▄▄█ ▒█▄▄▄█ ░▒█░░\n\n𝗥𝗶𝗭𝗼𝗲𝗟 ʙᴏᴛ sᴘᴀᴍ ʜᴇʀᴇ `{ms}` 𝗠𝗦")
    


@idk.on(events.NewMessage(incoming=True, pattern=r"\.reboot"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.reboot"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.reboot"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.reboot"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.reboot"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "𝗥𝗲𝗯𝗼𝗼𝘁𝗲𝗱\n\nPlease wait till it reboots..."
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await idk.disconnect()
        except Exception as e:
            pass
        try:
            await ydk.disconnect()
        except Exception as e:
            pass
        try:
            await wdk.disconnect()
        except Exception as e:
            pass
        try:
            await hdk.disconnect()
        except Exception as e:
            pass
        try:
            await sdk.disconnect()
        except Exception as e:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

       
@idk.on(events.NewMessage(incoming=True, pattern=r"\.robot"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.robot"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.robot"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.robot"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.robot"))
async def alive(event):
    if event.sender_id in SMEX_USERS:
     await idk.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption="♡︎ 𝐑ɪ𝐙ᴏᴇ𝐋 𝐁ᴏ𝐓 𝐒ᴘᴀ𝐌 ♡︎\n\n\n ✧ ʀɪᴢᴏᴇʟʟ sᴘᴀᴍ ɪᴢᴢ ᴀʟɪᴠᴇ ✧\n\n ┏━━━━━━━━━━━━━━━━━━━\n ┣➣ ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : 3.9.6\n ┣➣ ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : 1.17 \n ┣➣ sᴜᴘᴘᴏʀᴛ : [JOIN](https://t.me/DNHxHELL)\n ┣➣ ᴄʀᴇᴀᴛᴇʀ : [𝗥𝗶𝗭𝗼𝗲𝗟](https://t.me/TheRiZoeL)\n ┗━━━━━━━━━━━━━━━━━━━\n\n 🖤 [𝐑𝐄𝐏𝐎](https://github.com/MrRizoel/RiZoeLBotSpam) 🖤"                                
                              )
     await ydk.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption="♡︎ 𝐑ɪ𝐙ᴏᴇ𝐋 𝐁ᴏ𝐓 𝐒ᴘᴀ𝐌 ♡︎\n\n\n ✧ ʀɪᴢᴏᴇʟʟ sᴘᴀᴍ ɪᴢᴢ ᴀʟɪᴠᴇ ✧\n\n ┏━━━━━━━━━━━━━━━━━━━\n ┣➣ ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : 3.9.6\n ┣➣ ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : 1.17 \n ┣➣ sᴜᴘᴘᴏʀᴛ : [JOIN](https://t.me/DNHxHELL)\n ┣➣ ᴄʀᴇᴀᴛᴇʀ : [𝗥𝗶𝗭𝗼𝗲𝗟](https://t.me/TheRiZoeL)\n ┗━━━━━━━━━━━━━━━━━━━\n\n 🖤 [𝐑𝐄𝐏𝐎](https://github.com/MrRizoel/RiZoeLBotSpam) 🖤"                                
                              )
     await wdk.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption="♡︎ 𝐑ɪ𝐙ᴏᴇ𝐋 𝐁ᴏ𝐓 𝐒ᴘᴀ𝐌 ♡︎\n\n\n ✧ ʀɪᴢᴏᴇʟʟ sᴘᴀᴍ ɪᴢᴢ ᴀʟɪᴠᴇ ✧\n\n ┏━━━━━━━━━━━━━━━━━━━\n ┣➣ ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : 3.9.6\n ┣➣ ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : 1.17 \n ┣➣ sᴜᴘᴘᴏʀᴛ : [JOIN](https://t.me/DNHxHELL)\n ┣➣ ᴄʀᴇᴀᴛᴇʀ : [𝗥𝗶𝗭𝗼𝗲𝗟](https://t.me/TheRiZoeL)\n ┗━━━━━━━━━━━━━━━━━━━\n\n 🖤 [𝐑𝐄𝐏𝐎](https://github.com/MrRizoel/RiZoeLBotSpam) 🖤"                                
                              )
     await hdk.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption="♡︎ 𝐑ɪ𝐙ᴏᴇ𝐋 𝐁ᴏ𝐓 𝐒ᴘᴀ𝐌 ♡︎\n\n\n ✧ ʀɪᴢᴏᴇʟʟ sᴘᴀᴍ ɪᴢᴢ ᴀʟɪᴠᴇ ✧\n\n ┏━━━━━━━━━━━━━━━━━━━\n ┣➣ ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : 3.9.6\n ┣➣ ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : 1.17 \n ┣➣ sᴜᴘᴘᴏʀᴛ : [JOIN](https://t.me/DNHxHELL)\n ┣➣ ᴄʀᴇᴀᴛᴇʀ : [𝗥𝗶𝗭𝗼𝗲𝗟](https://t.me/TheRiZoeL)\n ┗━━━━━━━━━━━━━━━━━━━\n\n 🖤 [𝐑𝐄𝐏𝐎](https://github.com/MrRizoel/RiZoeLBotSpam) 🖤"                                
                              )
     await sdk.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption="♡︎ 𝐑ɪ𝐙ᴏᴇ𝐋 𝐁ᴏ𝐓 𝐒ᴘᴀ𝐌 ♡︎\n\n\n ✧ ʀɪᴢᴏᴇʟʟ sᴘᴀᴍ ɪᴢᴢ ᴀʟɪᴠᴇ ✧\n\n ┏━━━━━━━━━━━━━━━━━━━\n ┣➣ ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : 3.9.6\n ┣➣ ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : 1.17 \n ┣➣ sᴜᴘᴘᴏʀᴛ : [JOIN](https://t.me/DNHxHELL)\n ┣➣ ᴄʀᴇᴀᴛᴇʀ : [𝗥𝗶𝗭𝗼𝗲𝗟](https://t.me/TheRiZoeL)\n ┗━━━━━━━━━━━━━━━━━━━\n\n 🖤 [𝐑𝐄𝐏𝐎](https://github.com/MrRizoel/RiZoeLBotSpam) 🖤"                                
                              )        
        
        
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.bhelp"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bhelp"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bhelp"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bhelp"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bhelp"))
async def help(e):
    if e.sender_id in SMEX_USERS:
       text = "𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀\n\n𝙐𝙩𝙞𝙡𝙨 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.robot\n.bot\n.reboot\n\n𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.bio\n.bleave\n\n𝙎𝙥𝙖𝙢 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.bspam\n.dspam\n.bigbspam\n.fuk\n.replyfuk\n.dreplyfuk\n\n\nFor more help regarding usage of plugins type plugins name"
       await e.reply(text, parse_mode=None, link_preview=None )

        

    
        
text = """
┏━━┓━━┏━━━┓━━━━━━━━┏┓━
┃┏┓┃┏┓┃┏━┓┃━━━━━━━━┃┃━
┃┗┛┃┗┛┗┛━┛┃┏━━┓┏━━┓┃┃━
┃━━┛┏┓┃┏━┏┓┃┏┓┃┃┏┓┃┃┃━
┃┃┃┃┃┃┃┗━┛┃┃┗┛┃┃┃━┫┃┗━┓
┗┛┗┛┗┛┗━━━┛┗━━┛┗━━┛┗━━┛"""

print(text)
print("")
print("SMEX! Rɪᴢᴏᴇʟ ʙᴏᴛ sᴘᴀᴍ Started Sucessfully. TRY .robot To check")
if len(sys.argv) not in (1, 3, 4):
    try:
        idk.disconnect()
    except Exception as e:
        pass
    try:
        ydk.disconnect()
    except Exception as e:
        pass
    try:
        wdk.disconnect()
    except Exception as e:
        pass
    try:
        hdk.disconnect()
    except Exception as e:
        pass
    try:
        sdk.disconnect()
    except Exception as e:
        pass
else:
    try:
        idk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ydk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        wdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        hdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sdk.run_until_disconnected()
    except Exception as e:
        pass

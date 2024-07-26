from datetime import date as date_
import datetime
import os
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup)
import humanize
from helper.progress import humanbytes

from helper.database import insert, find_one, used_limit, usertype, uploadlimit, addpredata, total_rename, total_size
from pyrogram.file_id import FileId
from helper.database import daily as daily_
from helper.date import check_expi
import os

CHANNEL = os.environ.get('CHANNEL', "Yugen_Bots")
STRING = os.environ.get("STRING", "1BVtsOGcBu6e9YccONr7Bq1tbskWRjgU3vlwS9_TKx3Nh_HVoZbNVo5YZOagmwm3yqaHnPHKaGAztwtkCk4NzMFEMkQ8aYRwDbtsmbMjxMj-MBV_ySzDwOjBJGE_4Z8UUkWK1z70vNRy0Os2FNneR2CzNqWcZnEO69m_LlRdRnuj0kV_5Yaz9KNWndQAStOPsHIHbhiaAVV477MFMef8GqiqdX9imWCdzAeGNzMbnzff9WLjAXFXjRFaDVmWLRerFYeYoTMYLcfiskNtS8vgN72exzNGlcjb2K8q_5JL0bitWofpVh3DZ6Erc-1J9AqcN_zlh0pPoA3hvMlHdbdyOWhfYAAIBSvs=")
ADMIN = int(os.environ.get("ADMIN", 1484670284))
bot_username = os.environ.get("BOT_USERNAME","YugenRenameBot")
log_channel = int(os.environ.get("LOG_CHANNEL", "-1002080756028"))
token = os.environ.get('TOKEN', '7264999897:AAEOQeOGQQPLWcmvT8rv47Tfd2u_oaMGHCo')
botid = token.split(':')[0]
FLOOD = 0
LAZY_PIC = os.environ.get("LAZY_PIC", "https://telegra.ph/file/8fe5276a43438e5390909.jpg")


# Part of Day --------------------
currentTime = datetime.datetime.now()

if currentTime.hour < 12:
    wish = "❤️ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ꜱᴡᴇᴇᴛʜᴇᴀʀᴛ ❤️"
elif 12 <= currentTime.hour < 12:
    wish = '🤍 ɢᴏᴏᴅ ᴀꜰᴛᴇʀɴᴏᴏɴ ᴍʏ ʟᴏᴠᴇ 🤍'
else:
    wish = '🦋 ɢᴏᴏᴅ ᴇᴠᴇɴɪɴɢ ʙᴀʙʏ 🦋'

# -------------------------------


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    old = insert(int(message.chat.id))
    try:
        id = message.text.split(' ')[1]
    except:
        txt=f"""ʏᴏᴏ {message.from_user.mention}, \n\n
	ɪ ᴀᴍ ꜰɪʟᴇ ʀᴇɴᴀᴍᴇʀ ʙᴏᴛ, ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴛ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ**ᴅᴏᴄᴜᴍᴇɴᴛ ᴏʀ ᴠɪᴅᴇᴏ** ᴀɴᴅ ᴇɴᴛᴇʀ ɴᴇᴡ ꜰɪʟᴇɴᴀᴍᴇ ᴛᴏ ʀᴇɴᴀᴍᴇ ɪᴛ"""
        await message.reply_photo(photo=LAZY_PIC,
                                caption=txt,
                                reply_markup=InlineKeyboardMarkup(
                                      [[InlineKeyboardButton("🔺 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ 🔺", url="https://t.me/Yugen_Bots")],
                                      [InlineKeyboardButton("ʀᴇᴘᴏʀᴛ", url="https://t.me/Yugen_Bots_Support"),InlineKeyboardButton("ᴜᴘɢʀᴀᴅᴇ", callback_data='upgrade')],
                                      [InlineKeyboardButton("ɴᴇᴛᴡᴏʀᴋ", url='https://t.me/YugenNetwork')]
                                      ]))
        return
    if id:
        if old == True:
            try:
                await client.send_message(id, "ʏᴏᴜʀ ꜰʀɪᴇɴᴅ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴜꜱɪɴɢ ᴏᴜʀ ʙᴏᴛ")
                await message.reply_photo(photo=LAZY_PIC,
                                         caption=txt,
                                         reply_markup=InlineKeyboardMarkup(
                                            [[InlineKeyboardButton("🔺 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ 🔺", url="https://t.me/Yugen_Bots")],
                                      [InlineKeyboardButton("ʀᴇᴘᴏʀᴛ", url="https://t.me/Yugen_Bots_Support"),InlineKeyboardButton("ᴜᴘɢʀᴀᴅᴇ", callback_data='upgrade')],
                                      [InlineKeyboardButton("ɴᴇᴛᴡᴏʀᴋ", url='https://t.me/YugenNetwork')]
                                          ]))
            except:
                return
        else:
            await client.send_message(id, "ᴄᴏɴɢʀᴀᴛꜱ! ʏᴏᴜ ᴡᴏɴ 100ᴍʙ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ")
            _user_ = find_one(int(id))
            limit = _user_["uploadlimit"]
            new_limit = limit + 104857600
            uploadlimit(int(id), new_limit)
            await message.reply_text(text=f"""
	ʏᴏᴏ {message.from_user.first_name }\n\n
	__ɪ ᴀᴍ ꜰɪʟᴇ ʀᴇɴᴀᴍᴇʀ ʙᴏᴛ, ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴛ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ**ᴅᴏᴄᴜᴍᴇɴᴛ ᴏʀ ᴠɪᴅᴇᴏ** ᴀɴᴅ ᴇɴᴛᴇʀ ɴᴇᴡ ꜰɪʟᴇɴᴀᴍᴇ ᴛᴏ ʀᴇɴᴀᴍᴇ ɪᴛ__
	""", reply_to_message_id=message.id,
                                     reply_markup=InlineKeyboardMarkup(
                                     [[InlineKeyboardButton("🔺 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ 🔺", url="https://t.me/Yugen_Bots")],
                                      [InlineKeyboardButton("ʀᴇᴘᴏʀᴛ", url="https://t.me/Yugen_Bots_Support"),InlineKeyboardButton("ᴜᴘɢʀᴀᴅᴇ", callback_data='upgrade')],
                                      [InlineKeyboardButton("ɴᴇᴛᴡᴏʀᴋ", url='https://t.me/YugenNetwork')]
                                          ]))
    


@Client.on_message((filters.private & (filters.document | filters.audio | filters.video)) | filters.channel & (filters.document | filters.audio | filters.video))
async def send_doc(client, message):
    update_channel = CHANNEL
    user_id = message.from_user.id
    if update_channel:
        try:
            await client.get_chat_member(update_channel, user_id)
        except UserNotParticipant:
            _newus = find_one(message.from_user.id)
            user = _newus["usertype"]
            await message.reply_text("```ᴛᴏ ᴜꜱᴇ ᴍᴇ, ʏᴏᴜ ɢᴏᴛᴛᴀ ᴊᴏɪɴ ᴍʏ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ``` ",
                                     reply_to_message_id=message.id,
                                     reply_markup=InlineKeyboardMarkup(
                                         [[InlineKeyboardButton("👾 ʏᴜɢᴇɴ ʙᴏᴛꜱ 👾", url=f"https://t.me/{update_channel}")]]))
            await client.send_message(log_channel,f"👾 #RENAME_LOGS 👾,\n\n**ID** : `{user_id}`\n**Name**: {message.from_user.first_name} {message.from_user.last_name}\n**User-Plan** : {user}\n\n ",
                                                                                                       reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔺 Restrict User ( **pm** ) 🔺", callback_data="ceasepower")]]))
            return

    try:
        bot_data = find_one(int(botid))
        prrename = bot_data['total_rename']
        prsize = bot_data['total_size']
        user_deta = find_one(user_id)
    except:
        await message.reply_text("ᴜꜱᴇ ᴀʙᴏᴜᴛ ᴄᴍᴅ ꜰɪʀꜱᴛ /about")
    try:
        used_date = user_deta["date"]
        buy_date = user_deta["prexdate"]
        daily = user_deta["daily"]
        user_type = user_deta["usertype"]
    except:
        await message.reply_text(text=f"ʜᴇʟʟᴏ {message.from_user.mention}  **ᴡᴇ ᴀʀᴇ ᴄᴜʀʀᴇɴᴛʟʏ ᴡᴏʀᴋɪɴɢ ᴏɴ ᴛʜɪꜱ ɪꜱꜱᴜᴇ**\n\nᴘʟᴇᴀꜱᴇ ᴛʀʏ ᴛᴏ ʀᴇɴᴀᴍᴇ ꜰɪʟᴇꜱ ꜰʀᴏᴍ ʏᴏᴜʀ ᴀɴᴏᴛʜᴇʀ ᴀᴄᴄᴏᴜɴᴛ.\nʙᴇᴄᴀᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ᴄᴀɴ'ᴛ ʀᴇɴᴀᴍᴇ ꜰɪʟᴇ ꜱᴇɴᴛ ʙʏ ꜱᴏᴍᴇ ɪᴅꜱ.\n\nɪꜰ ʏᴏᴜ ᴀʀᴇ ᴀɴ ᴀᴅᴍɪɴ ᴅᴏɴ'ᴛ ᴡᴏʀʀʏ ! ʜᴇʀᴇ ᴡᴇ ʜᴀᴠᴇ ᴀ ꜱᴏʟᴜᴛɪᴏɴ ꜰᴏʀ ʏᴏᴜ ᴅᴇᴀʀ {message.from_user.mention}.\n\nᴘʟᴇᴀꜱᴇ ᴜꜱᴇ \n👉 `/addpremium your_other_userid` 👈 ᴛᴏ ᴜꜱᴇ ᴘʀᴇᴍɪᴜᴍ ꜰᴇᴀᴜᴛʀᴇꜱ\n\n",
                                  reply_markup=InlineKeyboardMarkup(
                                                                   [[InlineKeyboardButton("🔺 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ 🔺", url="https://t.me/Yugen_Bots")],
                                      [InlineKeyboardButton("ʀᴇᴘᴏʀᴛ", url="https://t.me/Yugen_Bots_Support"),InlineKeyboardButton("ᴜᴘɢʀᴀᴅᴇ", callback_data='upgrade')],
                                      [InlineKeyboardButton("ɴᴇᴛᴡᴏʀᴋ", url='https://t.me/YugenNetwork')]
                                                                    ])
				)
        await message.reply_text(text=f"👾")
        return 

    c_time = time.time()

    if user_type == "Free":
        LIMIT = 100
    else:
        LIMIT = 0
    then = used_date + LIMIT
    left = round(then - c_time)
    conversion = datetime.timedelta(seconds=left)
    ltime = str(conversion)
    if left > 0:
        await message.reply_text(f"```ꜱᴏʀʀʏ ᴅᴜᴅᴇ ɪ ᴀᴍ ɴᴏᴛ ᴏɴʟʏ ꜰᴏʀ ʏᴏᴜ \n ꜰʟᴏᴏᴅ ᴄᴏɴᴛʀᴏʟ ɪꜱ ᴀᴄᴛɪᴠᴇ ꜱᴏ ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ ꜰᴏʀ {ltime}```", reply_to_message_id=message.id)
    else:
        # Forward a single message
        media = await client.get_messages(message.chat.id, message.id)
        file = media.document or media.video or media.audio
        dcid = FileId.decode(file.file_id).dc_id
        filename = file.file_name
        value = 2147483648
        used_ = find_one(message.from_user.id)
        used = used_["used_limit"]
        limit = used_["uploadlimit"]
        expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
        if expi != 0:
            today = date_.today()
            pattern = '%Y-%m-%d'
            epcho = int(time.mktime(time.strptime(str(today), pattern)))
            daily_(message.from_user.id, epcho)
            used_limit(message.from_user.id, 0)
        remain = limit - used
        if remain < int(file.file_size):
            await message.reply_text(f"100% ᴏꜰ ᴅᴀɪʟʏ {humanbytes(limit)} ᴅᴀᴛᴀ Qᴜᴏᴛᴀ ᴇxʜᴀᴜꜱᴛᴇᴅ.\n\n  ꜰɪʟᴇ ꜱɪᴢᴇ ᴅᴇᴛᴇᴄᴛᴇᴅ {humanbytes(file.file_size)}\n  ᴜꜱᴇᴅ ᴅᴀɪʟʏ ʟɪᴍɪᴛ {humanbytes(used)}\n\nʏᴏᴜ ʜᴀᴠᴇ ᴏɴʟʏ **{humanbytes(remain)}** ʟᴇꜰᴛ ᴏɴ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ.\nɪꜰ ᴜ ᴡᴀɴᴛ ᴛᴏ ʀᴇɴᴀᴍᴇ ʟᴀʀɢᴇ ꜰɪʟᴇ ᴜᴘɢʀᴀᴅᴇ ʏᴏᴜʀ ᴘʟᴀɴ ", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ᴜᴘɢʀᴀᴅᴇ 💳", callback_data="upgrade")]]))
            return
        if value < file.file_size:
            
            if STRING:
                if buy_date == None:
                    await message.reply_text(f" ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜᴘʟᴏᴀᴅ ᴍᴏʀᴇ ᴛʜᴇɴ {humanbytes(limit)} ᴜꜱᴇᴅ ᴅᴀɪʟʏ ʟɪᴍɪt {humanbytes(used)} ", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ᴜᴘɢʀᴀᴅᴇ 💳", callback_data="upgrade")]]))
                    return
                pre_check = check_expi(buy_date)
                if pre_check == True:
                    await message.reply_text(f"""__ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ᴅᴏ ᴡɪᴛʜ ᴛʜɪꜱ ꜰɪʟᴇ?__\n**ꜰɪʟᴇ ɴᴀᴍᴇ** : `{filename}`\n**ꜰɪʟᴇ ꜱɪᴢᴇ** : {humanize.naturalsize(file.file_size)}\n**ᴅᴄ ɪᴅ** : {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 ʀᴇɴᴀᴍᴇ", callback_data="rename"), InlineKeyboardButton("✖️ ᴄᴀɴᴄᴇʟ", callback_data="cancel")]]))
                    total_rename(int(botid), prrename)
                    total_size(int(botid), prsize, file.file_size)
                else:
                    uploadlimit(message.from_user.id, 1288490188)
                    usertype(message.from_user.id, "Free")

                    await message.reply_text(f'Your Plan Expired On {buy_date}', quote=True)
                    return
            else:
                await message.reply_text("ᴄᴀɴ'ᴛ ᴜᴘʟᴏᴀᴅ ꜰɪʟᴇꜱ ʙɪɢɢᴇʀ ᴛʜᴀɴ 2ɢʙ")
                return
        else:
            if buy_date:
                pre_check = check_expi(buy_date)
                if pre_check == False:
                    uploadlimit(message.from_user.id, 1288490188)
                    usertype(message.from_user.id, "Free")

            filesize = humanize.naturalsize(file.file_size)
            fileid = file.file_id
            total_rename(int(botid), prrename)
            total_size(int(botid), prsize, file.file_size)
            await message.reply_text(f"""__ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ᴅᴏ ᴡɪᴛʜ ᴛʜɪꜱ ꜰɪʟᴇ?__\n**ꜰɪʟᴇ ɴᴀᴍᴇ** : `{filename}`\n**ꜰɪʟᴇ ꜱɪᴢᴇ** : {humanize.naturalsize(file.file_size)}\n**ᴅᴄ ɪᴅ** : {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 ʀᴇɴᴀᴍᴇ", callback_data="rename"), InlineKeyboardButton("✖️ ᴄᴀɴᴄᴇʟ", callback_data="cancel")]]))
                    

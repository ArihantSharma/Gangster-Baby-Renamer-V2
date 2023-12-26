import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ : <a href="https://t.me/+RfAjS_m9WLg1OTE1">ʏᴜɢᴇɴ ʙᴏᴛꜱ</a>\nᴏᴡɴᴇʀ : {user.mention}\nʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ\nᴛᴏᴛᴀʟ ʀᴇɴᴀᴍᴇᴅ ꜰɪʟᴇ :- {total_rename}\nᴛᴏᴛᴀʟ ꜱɪᴢᴇ ʀᴇɴᴀᴍᴇᴅ :- {humanbytes(int(total_size))}\n\n```Thank you for all of your support```",quote=True)

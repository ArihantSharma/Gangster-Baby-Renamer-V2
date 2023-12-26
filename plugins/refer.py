from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
@Client.on_message(filters.private & filters.command(["refer"]))
async def refer(client,message):
    reply_markup = InlineKeyboardMarkup(
       		[[ InlineKeyboardButton("ꜱʜᴀʀᴇ ʏᴏᴜʀ ʟɪɴᴋ" ,url=f"https://t.me/share/url?url=https://t.me/TestRename4GBot?start={message.from_user.id}") ]   ])
    await message.reply_text(f"ʀᴇꜰᴇʀ ᴀɴᴅ ᴇᴀʀɴ ɢᴇᴛ 100ᴍʙ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ\nᴘᴇʀ ʀᴇꜰᴇʀ 100ᴍʙ\n ʏᴏᴜʀ ʟɪɴᴋ :- https://t.me/TestRename4GBot?start={message.from_user.id} ",reply_to_message_id = message.id,reply_markup=reply_markup,)
    

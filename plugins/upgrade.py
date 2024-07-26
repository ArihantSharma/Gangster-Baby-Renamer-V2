"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Fʀᴇᴇ Usᴇʀ Pʟᴀɴ**
	__ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 1.2ɢʙ
        ᴘᴀʏ ʀꜱ 0 ᴘᴇʀ ᴍᴏɴᴛʜ__
	
	**Bᴇɢɪɴɴᴇʀ Pʟᴀɴ** 
	__ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 10ɢʙ
        ᴘᴀʏ ʀꜱ 20 ᴘᴇʀ ᴍᴏɴᴛʜ__
	
	**Iɴᴛᴇʀᴍᴇᴅɪᴀᴛᴇ Pʟᴀɴ**
	__ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 50ɢʙ
        ᴘᴀʏ ʀꜱ 45 ᴘᴇʀ ᴍᴏɴᴛʜ__
	
	**Pʀᴏ Pʟᴀɴ**
	__ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 100ɢʙ
        ᴘᴀʏ ʀꜱ 70 ᴘᴇʀ ᴍᴏɴᴛʜ__
	
	
	ᴘᴀʏ ᴜꜱɪɴɢ ᴜᴘɪ ɪᴅ `yugenbots@ibl`
	
	```ᴀꜰᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ ꜱᴇɴᴅ ᴛʜᴇ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴛᴏ ᴀɴʏ ᴏꜰ ᴛʜᴇ ᴀᴅᴍɪɴꜱ```"""
	keybord = InlineKeyboardMarkup([
        			InlineKeyboardButton("ᴀᴅᴍɪɴ",url = "https://t.me/voatcb"), 
        			[InlineKeyboardButton("20₹",url = "https://pay.upilink.in/pay/yugenbots@ibl?am=20"),
        			InlineKeyboardButton("45₹",url = "https://pay.upilink.in/pay/yugenbots@ibl?am=45"),
        			InlineKeyboardButton("70₹",url = "https://pay.upilink.in/pay/yugenbots@ibl?am=70")],[InlineKeyboardButton("ᴄᴀɴᴄᴇʟ",callback_data = "cancel")]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Fʀᴇᴇ Usᴇʀ Pʟᴀɴ**
	__ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 1.2ɢʙ
        ᴘᴀʏ ʀꜱ 0 ᴘᴇʀ ᴍᴏɴᴛʜ__
	
	**Bᴇɢɪɴɴᴇʀ Pʟᴀɴ** 
	__ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 10ɢʙ
        ᴘᴀʏ ʀꜱ 20 ᴘᴇʀ ᴍᴏɴᴛʜ__
	
	**Iɴᴛᴇʀᴍᴇᴅɪᴀᴛᴇ Pʟᴀɴ**
	__ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 50ɢʙ
        ᴘᴀʏ ʀꜱ 45 ᴘᴇʀ ᴍᴏɴᴛʜ__
	
	**Pʀᴏ Pʟᴀɴ**
	__ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 100ɢʙ
        ᴘᴀʏ ʀꜱ 70 ᴘᴇʀ ᴍᴏɴᴛʜ__
	
	
	ᴘᴀʏ ᴜꜱɪɴɢ ᴜᴘɪ ɪᴅ `yugenbots@ibl`
	
	```ᴀꜰᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ ꜱᴇɴᴅ ᴛʜᴇ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴛᴏ ᴀɴʏ ᴏꜰ ᴛʜᴇ ᴀᴅᴍɪɴꜱ```"""
	keybord = InlineKeyboardMarkup([
        			InlineKeyboardButton("ᴀᴅᴍɪɴ",url = "https://t.me/voatcb"), 
        			[InlineKeyboardButton("20₹",url = "https://pay.upilink.in/pay/yugenbots@ibl?am=20"),
        			InlineKeyboardButton("45₹",url = "https://pay.upilink.in/pay/yugenbots@ibl?am=45"),
        			InlineKeyboardButton("70₹",url = "https://pay.upilink.in/pay/yugenbots@ibl?am=70")],[InlineKeyboardButton("ᴄᴀɴᴄᴇʟ",callback_data = "cancel")]])

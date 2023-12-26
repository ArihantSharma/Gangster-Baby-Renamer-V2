"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price Rs 66  ind /🌎 0.8$  per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price Rs 100  ind /🌎 1.2$  per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Price Rs 206  ind /🌎 2.5$  per Month
	
	
	Pay Using Upi I'd ```7808912076@paytm```
	
	After Payment Send Screenshots Of 
        Payment To Admin @mRiderDM"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ᴀᴅᴍɪɴ 1",url = "https://t.me/iwilltouchyoulilnigga"),InlineKeyboardButtln("ᴀᴅᴍɪɴ 2",url = "https://t.me/Sixteen_Years_Older")], 
        			[InlineKeyboardButton("20₹",url = "https://telegra.ph/file/d4dd2eff91963bce9f283.jpg"),
        			InlineKeyboardButton("45₹",url = "https://telegra.ph/file/4ce4ddd7c34420344247e.jpg"),
        			InlineKeyboardButton("80₹",url = "https://telegra.ph/file/cc0fb7ac7348ebb6d56a6.jpg")],[InlineKeyboardButton("ᴄᴀɴᴄᴇʟ",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price Rs 66  ind /🌎 0.8$  per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price Rs 100  ind /🌎 1.2$  per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Price Rs 206  ind /🌎 2.5$  per Month
	
	
	Pay Using Upi I'd ```7808912076@paytm```
	
	After Payment Send Screenshots Of 
        Payment To Admin @mRiderDM"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ᴀᴅᴍɪɴ 1",url = "https://t.me/iwilltouchyoulilnigga"),InlineKeyboardButtln("ᴀᴅᴍɪɴ 2",url = "https://t.me/Sixteen_Years_Older")], 
        			[InlineKeyboardButton("20₹",url = "https://telegra.ph/file/d4dd2eff91963bce9f283.jpg"),
        			InlineKeyboardButton("45₹",url = "https://telegra.ph/file/4ce4ddd7c34420344247e.jpg"),
        			InlineKeyboardButton("80₹",url = "https://telegra.ph/file/cc0fb7ac7348ebb6d56a6.jpg")],[InlineKeyboardButton("ᴄᴀɴᴄᴇʟ",callback_data = "cancel")  ]])

"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price Rs 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price Rs 20 per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price Rs 45 per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Price Rs 80 per Month
	
	
	Pay Using Upi I'd `arihantsharmaofficial@oksbi`
	
	After Payment Send Screenshots Of 
        Payment To Admins"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ᴀᴅᴍɪɴ 1",url = "https://t.me/iwilltouchyoulilnigga"),InlineKeyboardButton("ᴀᴅᴍɪɴ 2",url = "https://t.me/Sixteen_Years_Older")], 
        			[InlineKeyboardButton("20₹",url = "upi://pay?pa=arihantsharmaofficial@oksbi&pn=Arihant%20Sharma&am=20.00&cu=INR&aid=uGICAgMDAwIqrXQ"),
        			InlineKeyboardButton("45₹",url = "upi://pay?pa=arihantsharmaofficial@oksbi&pn=Arihant%20Sharma&am=45.00&cu=INR&aid=uGICAgMDAwIqrXQ"),
        			InlineKeyboardButton("80₹",url = "upi://pay?pa=arihantsharmaofficial@oksbi&pn=Arihant%20Sharma&am=80.00&cu=INR&aid=uGICAgMDAwIqrXQ")],[InlineKeyboardButton("ᴄᴀɴᴄᴇʟ",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price Rs 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price Rs 20 per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price Rs 45 per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Price Rs 80 per Month
	
	
	Pay Using Upi I'd `arihantsharmaofficial@oksbi`
	
	After Payment Send Screenshots Of 
        Payment To Admins"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ᴀᴅᴍɪɴ 1",url = "https://t.me/iwilltouchyoulilnigga"),InlineKeyboardButton("ᴀᴅᴍɪɴ 2",url = "https://t.me/Sixteen_Years_Older")], 
        			[InlineKeyboardButton("20₹",url = "upi://pay?pa=arihantsharmaofficial@oksbi&pn=Arihant%20Sharma&am=20.00&cu=INR&aid=uGICAgMDAwIqrXQ"),
        			InlineKeyboardButton("45₹",url = "upi://pay?pa=arihantsharmaofficial@oksbi&pn=Arihant%20Sharma&am=45.00&cu=INR&aid=uGICAgMDAwIqrXQ"),
        			InlineKeyboardButton("80₹",url = "upi://pay?pa=arihantsharmaofficial@oksbi&pn=Arihant%20Sharma&am=80.00&cu=INR&aid=uGICAgMDAwIqrXQ")],[InlineKeyboardButton("ᴄᴀɴᴄᴇʟ",callback_data = "cancel")  ]])

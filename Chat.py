# Bu modul 29.01.2023 tarixində

# aykhan026 və @guliyev di (Famil) tərəfindən yazılıb # License: https://github.com/aykhan@26/AykhanRoBot/LICENSE

# Kodu kiməsə satmaq qadağandır!

#GitHub: aykhan026 # Telegram: @aykhan_s | @guliyev_di

from Aykhan import * from Aykhan.komekci.mesajlar.mesaj import salam, necesen, sagol, getdim, geldim, ban

active_chats = []

# Chatbot açıb bağlamaq üçün manual modul aykhan@26

@aykhan2.on_message(filters.command("chatbot") & filters.user(SAHIB))

async def chatbot_status(, message):

global active_chats

if len(message.command) != 2: await message.reply_text("/chatbot [ON] va yaxud [OFF] yazmadınız")

return

status = message.text.split(None, 1)[1] chat_id = message.chat.id

if status == "ON" or status = "on" or status = "On":

if chat_id not in active_chats: active_chats.append(chat_id)

text = "ChatBot bu qrupda aktiv olundu !"

await message.reply_text(text)

return

await message.reply_text("ChatBot onsuzda aktivdir !*)

return

elif status == "OFF" or status = "off" or status = "Off":

if chat_id in active_chats: active_chats.remove(chat_id)

await message.reply_text("ChatBot bu qrupda deaktiv olundu !")

return

awalt message.reply_text("ChatBot onsuzda deaktivdir !") return

else:

await message.reply_text("/chatbot [ON] və yaxud [OFF] yazmadınız")

@aykhan2.on_message(filters.text)

async def start(_, msg: Message):

global active_chats text = msg.text.lower()

chat_id = msg.chat.id

if msg.chat.id not in active_chats:

return if "salam" in text:

await msg.reply_text(f(random.choice(salam)}") if "necǝsən" in text or "necesen" in text or "netersen" in text:

await msg.reply_text(ffrandom.choice(necesen)}")

if "sagol" in text or "sağol" in text or "saqol" in text: await msg.reply_text("frandom. choice( sagol)}")

if "getdim" in text or "gedim" in text or "gediram" in text or "gedirem" in text:

await msg.reply_text(f(random.choice(getdim)}") if "geldim" in text or "galdim" in text or "gal" in text or "galiram" in text:

await msg.reply_text(f" (random.choice(geldim)}")

if "ban" in text or "mute" in text or "purge" in text or "gban" in text: awalt msg.reply_text("{random.choice(ban)}")
import random
import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

app = Client(
    "filter-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):

    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🎬 Trixel Movie Group", url="https://t.me/trixel_movies")],
            [InlineKeyboardButton("➕ Add Me To Your Group", url="@tony_stark_v3_bot?startgroup=true")],
            [InlineKeyboardButton("📸 Instagram", url="https://www.instagram.com/sreehari_._pradeep?igsh=YWMzMzRzZWx2dWFy")],
            [InlineKeyboardButton("ℹ️ About Bot", callback_data="about_bot")]
        ]
    )

    images = ["https://graph.org/file/62386b57bf0394d7bd917-959daf5976f788890f.jpg", "https://graph.org/file/45f2868f0396506971dd4-319c9643069396cfbb.jpg", "https://graph.org/file/1d87e8717b0675ac15730-c491930774a108b163.jpg"]
    selected_image = random.choice(images)

    await message.reply_photo(
        photo=open(selected_image, "rb"),
        caption=(
            "🍿 **Welcome!** 🍿\n\n"
            "I am the filter bot of the **Trixel Movie group** 🎬\n"
            "You can add me to your group and use me.\n\n"
            "🍿 **സ്വാഗതം!** 🍿\n\n"
            "ഞാൻ **Trixel Movie 🎬 ഗ്രൂപ്പിന്റെ ഫിൽട്ടർ ബോട്ട്** ആണ്.\n"
            "നിങ്ങൾ എന്നെ നിങ്ങളുടെ **Group / Channel-ൽ add ചെയ്ത്** ഉപയോഗിക്കാം ☺️"
        ),
        reply_markup=buttons
    )

@app.on_callback_query(filters.regex("^about_bot$"))
async def about_bot(client, callback_query):

    about_text = (
        "╭────[ ᴍʏ ᴅᴇᴛᴀɪʟs ]────⍟\n"
        "├⍟ Mʏ Nᴀᴍᴇ : Tony Stark\n"
        "├⍟ Dᴇᴠᴇʟᴏᴘᴇʀ : Sreehari\n"
        "├⍟ Lɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ\n"
        "├⍟ Lᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ 𝟹\n"
        "├⍟ Dᴀᴛᴀʙᴀsᴇ : ᴍᴏɴɢᴏ ᴅʙ\n"
        "├⍟ Bᴏᴛ Sᴇʀᴠᴇʀ : Render\n"
        "├⍟ Bᴜɪʟᴅ Sᴛᴀᴛᴜs : ᴠ1.4 [ ꜱᴛᴀʙʟᴇ ]\n"
        "╰───────────────⍟"
    )

    await callback_query.message.reply_text(about_text)
    await callback_query.answer()

print("Bot Started...")
app.run()

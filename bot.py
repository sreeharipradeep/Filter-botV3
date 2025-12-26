import os
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ================= CONFIG =================
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

# =========================================

app = Client(
    "filter_bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

# ---------- START COMMAND ----------
@app.on_message(filters.command("start"))
async def start(client, message):

    images = ["start1.jpg", "start2.jpg", "start3.jpg"]
    selected_image = random.choice(images)

    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("👤 ABOUT", callback_data="about")],
            [InlineKeyboardButton("📢 Updates", url="https://t.me/your_channel")]
        ]
    )

    await message.reply_photo(
        photo=open(selected_image, "rb"),
        caption=(
            "👋 **Welcome to File Filter Bot**\n\n"
            "📌 Use `/filter` command\n"
            "📌 Send keywords to search files"
        ),
        reply_markup=buttons
    )

# ---------- ABOUT BUTTON ----------
@app.on_callback_query(filters.regex("about"))
async def about_callback(client, callback):

    text = (
        "╭────[ ᴍʏ ᴅᴇᴛᴀɪʟs ]────⍟\n"
        "├⍟ **My Name :** Tony Stark\n"
        "├⍟ **Developer :** Sreehari\n"
        "├⍟ **Library :** Pyrogram\n"
        "├⍟ **Language :** Python 3\n"
        "├⍟ **Database :** Mongo DB\n"
        "├⍟ **Bot Server :** Render\n"
        "├⍟ **Build Status :** v1.4 Stable\n"
        "╰───────────────⍟"
    )

    await callback.message.reply_text(text)

# ---------- FILTER COMMAND ----------
@app.on_message(filters.command("filter"))
async def filter_command(client, message):
    await message.reply_text(
        "🔍 **Filter Mode Enabled**\n\n"
        "Now send any keyword to search files."
    )

# ---------- TEXT MESSAGE ----------
@app.on_message(filters.text & ~filters.command())
async def text_handler(client, message):
    keyword = message.text
    await message.reply_text(
        f"📁 You searched for: **{keyword}**\n\n"
        "⚠️ File system not connected yet."
    )

# ---------- RUN BOT ----------
print("🤖 Bot is running...")
app.run()

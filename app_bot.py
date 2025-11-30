from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "TOKEN"  # <- вставь сюда токен своего бота

# Функция старт
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("YouTube", url="https://youtube.com/")],
        [InlineKeyboardButton("Instagram", url="https://instagram.com/")],
        [InlineKeyboardButton("TikTok", url="https://www.tiktok.com/")],
        [InlineKeyboardButton("Facebook", url="https://facebook.com/")],
        [InlineKeyboardButton("VK", url="https://vk.com/")],
        [InlineKeyboardButton("Discord", url="https://discord.com/")],
        [InlineKeyboardButton("Telegram", url="https://telegram.org/")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Привет! Выбери платформу, чтобы перейти:",
        reply_markup=reply_markup
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    
    print("Бот запущен...")
    app.run_polling()

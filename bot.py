from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎩 Merhaba ben Mr. Play. Centilmenliğin ve casinonun kesiştiği yerdeyiz.\n"
        "Hazırsan şans oyunlarına stil katarız!"
    )

async def tip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👔 Centilmenlik Tüyosu: Kazanmak doğaldır, ama şık kaybetmek gerçek zarafettir."
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("tip", tip))
    app.run_polling()

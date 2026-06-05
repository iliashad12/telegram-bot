from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from Scraping import get_average_price

Token = "8772360892:AAE7fYlmI9xQ1aQTcuUjFxym4DwWE2LBsVI"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام👋 قیمت محصولی که میخوای رو بفرست")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text

    try:
        avg = get_average_price(user_input)
        if avg is None:
            await update.message.reply_text("چیزی پیدا نشد، نام مصحول را درست وارد کنید ⚠️")
            return
        await update.message.reply_text(f"میانگین قیمت : {format(avg, ",")} تومان\n  محصول بعدی که میخوای رو بگو😊")
    except Exception:
        await update.message.reply_text("خطا در پردازش رخ داده، لطفا دوباره امتحان کنید ⚠️")


def main():
    app = Application.builder().token(Token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()


if __name__ == "__main__":
    main()
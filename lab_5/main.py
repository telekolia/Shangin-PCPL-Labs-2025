import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.WARNING)

with open("Telekolia_bot_token.txt") as f:
    TOKEN = f.read().strip()

START_MESSAGE = "Привет! 👋\nЯ простой бот с кнопками.\nВыберите опцию ниже:"

async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [[KeyboardButton("ℹ️ Информация")], [KeyboardButton("📞 Контакты")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(START_MESSAGE, reply_markup=reply_markup)

async def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    if text == "ℹ️ Информация":
        await update.message.reply_text("Это простой бот пока тут нет функционала, просто лабараторная работа вот такая.")
    elif text == "📞 Контакты":
        await update.message.reply_text("Контакты: @telekolja")
    else:
        await update.message.reply_text("Тсс..используйте кнопки.")

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT, handle_message))

    print("Бот запущен в упрощенном режиме...")
    application.run_polling()

if __name__ == '__main__':
    main()

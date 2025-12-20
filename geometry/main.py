import os
from telegram import  Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)
from model import get_solution
from decouple import config

TOKEN = config("TOKEN")






async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    subjects = """Г - Геометрія
А - Алгебра
Х - Хімія"""
    await update.message.reply_html(
        "Привіт!Це бот який допомагає вирішувати домашні завдання.Для того щоб скинути завдання відправте скріншот завдання з підписом - перша літера назву предмету(велика).",
    )
    await update.message.reply_html(
        subjects
    )
    



async def solution(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Shows the help message when the command /help is issued."""
    user_choice = update.message.caption
    photo_file = await update.message.photo[-1].get_file()
    await photo_file.download_to_drive("ex.jpg")
    if user_choice == "Г":
        text = get_solution("Геометрія")
        os.remove("ex.jpg")
        await update.message.reply_text(
            text= text,
        )
    elif user_choice == "А":
        text = get_solution("Алгебра")
        os.remove("ex.jpg")
        await update.message.reply_text(
            text= text,
        )
    elif user_choice == "Х":
        text = get_solution("Хімія")
        os.remove("ex.jpg")
        await update.message.reply_text(
            text= text,
        )
    elif user_choice == "Ф":
        text = get_solution("Фізика")
        os.remove("ex.jpg")
        await update.message.reply_text(
            text= text,
        )

def main() -> None:
    """Start the bot."""

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    
    
    application.add_handler(MessageHandler(filters.PHOTO & filters.CAPTION, solution))
    

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
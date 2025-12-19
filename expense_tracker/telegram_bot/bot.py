from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import date
from telegram import ReplyKeyboardMarkup

keyboard = [
    ["Add expense", "Show expenses"],
    ["Total", "Exit"]
]

reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

TOKEN = "your_token"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет 👋\n"
        "Я бот для учёта расходов.\n\n"
        "Команды:\n"
        "/add сумма категория\n"
        "/total"
        "Выберите действие:",
        reply_markup=reply_markup
    )

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        amount = float(context.args[0])
        category = context.args[1]

        with open("expenses.txt", "a") as file:
            file.write(f"{date.today()} | {category} | {amount}\n")

        await update.message.reply_text("Расход добавлен")
    except:
        await update.message.reply_text("Используй: /add 100 Food")

async def total(update: Update, context: ContextTypes.DEFAULT_TYPE):
    total_sum = 0
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                total_sum += float(line.strip().split(" | ")[2])
        await update.message.reply_text(f"💰 Всего потрачено: {total_sum}")
    except FileNotFoundError:
        await update.message.reply_text("Нет расходов")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("add", add))
app.add_handler(CommandHandler("total", total))

print("Bot is running...")
app.run_polling()

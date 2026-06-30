from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random
import json
import os

# PUT YOUR REAL TOKEN HERE
TOKEN = "8993780722:AAEu7-cVJ9kPqFmC6LHGaAUzkOdUKsWOFf8"

DATA_FILE = "data.json"

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        user_stats = json.load(f)
else:
    user_stats = {}

def save():
    with open(DATA_FILE, "w") as f:
        json.dump(user_stats, f)

def get_user(user_id):
    uid = str(user_id)
    if uid not in user_stats:
        user_stats[uid] = {"power": 0}
    return user_stats[uid]

def get_level(power):
    return power // 50 + 1

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💪 Gym Bot is online! Type /grow")

async def grow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = str(update.effective_user.id)
    stats = get_user(uid)

    change = random.randint(-5, 20)

    stories = [
        "🏋️ You kicked ASS on leg day and now your booty is HUGE!",
        "💪 You push through the pain and it paid off! your booty is growing!",
        "🔥 You did 20 squats at the gym! keep up the good work!",
        "🍑 You flew out  to see Dr. Miami and got a BBL! Your ass is bigger than Kim Kardashian!",
        "🍆 You got backshots from the neighbor! we all know anal makes your ass huge!",
    "you worked out with priscilla the muscle mommy! now yall are twins and have matching bootys!",
]
    stats["power"] += change
    save()

    level = get_level(stats["power"])

    await update.message.reply_text(
        f"{random.choice(stories)}\n\n"
        f"{'+' if change >= 0 else ''}{change} XP\n"
        f"🏆 Power: {stats['power']}\n"
        f"⭐ Level: {level}"
    )

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = str(update.effective_user.id)
    stats = get_user(uid)

    await update.message.reply_text(
        f"🏆 Power: {stats['power']}\n⭐ Level: {get_level(stats['power'])}"
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("growbooty", grow))
    app.add_handler(CommandHandler("stats", stats))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

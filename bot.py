from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from mcstatus import JavaServer

TOKEN = "8584566887:AAEI7OpsvG8-rq6bq6qO3s3BKqu64QidtSY"
SERVER_IP = "dinomc.org"  # ប្ដូរ IP របស់អ្នក
SERVER_PORT = 19132

def status(update: Update, context: CallbackContext):
    try:
        server = JavaServer(SERVER_IP, SERVER_PORT)
        status = server.status()
        reply = f"✅ Server Online\nPlayers: {status.players.online}/{status.players.max}\nPing: {status.latency} ms"
    except Exception as e:
        reply = "❌ Server Offline or cannot reach server."
    update.message.reply_text(reply)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("👋 សួស្ដី! ប្រើ /status ដើម្បីពិនិត្យ Minecraft Server Status")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("status", status))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

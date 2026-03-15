from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from mcstatus import JavaServer
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = "8584566887:AAEI7OpsvG8-rq6bq6qO3s3BKqu64QidtSY"
SERVER_IP = "dinomc.org"  # Minecraft server IP (no port needed, default 25565)

# /start command
def start(update: Update, context: CallbackContext):
    message = (
        "👋 សួស្ដី! សូមស្វាគមន៍ទៅ Telegram Bot Minecraft Status.\n"
        "ប្រើ commands ខាងក្រោម:\n"
        "/start - greet + show all commands\n"
        "/ip - show Minecraft server IP\n"
        "/status - show server status online/offline + players count/max"
    )
    update.message.reply_text(message)

# /ip command
def ip(update: Update, context: CallbackContext):
    update.message.reply_text(f"🖥️ Minecraft Server IP: {SERVER_IP}")

# /status command
def status(update: Update, context: CallbackContext):
    try:
        server = JavaServer(SERVER_IP)  # default port 25565
        status = server.status()
        reply = (
            f"✅ Server Online\n"
            f"Players: {status.players.online}/{status.players.max}\n"
            f"Ping: {status.latency} ms"
        )
    except Exception:
        reply = "❌ Server Offline or cannot reach server."
    update.message.reply_text(reply)

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ip", ip))
    dp.add_handler(CommandHandler("status", status))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

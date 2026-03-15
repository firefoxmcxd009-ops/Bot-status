# Telegram Minecraft Server Status Bot (No Port Needed)

Commands:
- /start : Greeting + show all commands
- /ip : Show Minecraft server IP
- /status : Show server status online/offline + players count/max

Deployment:
1. Replace YOUR_TELEGRAM_BOT_TOKEN in bot.py
2. Replace SERVER_IP with your Minecraft server IP
3. Test locally: python bot.py
4. Deploy to Render (Free):
   - Build Command: pip install -r requirements.txt
   - Start Command: python bot.py
Bot will run 24/7 and reply correctly

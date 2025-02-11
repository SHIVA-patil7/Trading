# 🪙 Meme Coin Trading Bot

This is a Django-based REST API that fetches new meme coins from the Solana blockchain, filters profitable coins, and simulates automated trading.

## 🚀 Features
- ✅ Fetch new meme coins from [DEX Screener API](https://dexscreener.com/)
- ✅ Filter meme coins based on price and liquidity
- ✅ Simulate buying and selling of meme coins
- ✅ Store meme coin data in MySQL

## 🛠 Tech Stack
- **Backend**: Django, Django REST Framework
- **Database**: MySQL
- **External API**: DEX Screener API
- **Dependencies**: `Django`, `djangorestframework`, `requests`

---

## 📌 Installation Guide

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/meme-coin-trading-bot.git
cd meme-coin-trading-bot


python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'meme_coin_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

RUN THE COMANDS

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
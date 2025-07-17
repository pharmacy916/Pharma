import requests

def log_to_telegram(bot_token, chat_id, message):
    try:
        url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        payload = {
            'chat_id': chat_id,
            'text': message
        }
        res = requests.post(url, data=payload)
        res.raise_for_status()
    except Exception as e:
        print(f"[TELEGRAM LOGGING ERROR] {e}")
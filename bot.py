import feedparser
import requests
import time
import os

TWITTER_USER = "puntingprofits"
BOT_TOKEN = os.getenv("8518789928:AAGEx1Fo7mzm_31EtcGe8yyS1rLrDxA7YoU")
CHAT_ID = os.getenv("CHAT_ID")

RSS_URL = f"https://nitter.net/{TWITTER_USER}/rss"

last_link = None

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message,
        "disable_web_page_preview": False
    }
    requests.post(url, data=data)

while True:
    try:
        feed = feedparser.parse(RSS_URL)
        if feed.entries:
            latest = feed.entries[0]
            if latest.link != last_link:
                last_link = latest.link
                msg = f"New tweet from @puntingprofits:\n{latest.title}\n{latest.link}"
                send_telegram(msg)
    except Exception as e:
        print("Error:", e)

    time.sleep(60)

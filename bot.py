
import requests
import time
import feedparser
import requests
import time

TWITTER_USER = "puntingprofits"
BOT_TOKEN = "8518789928:AAGEx1Fo7mzm_31EtcGe8yyS1rLrDxA7YoU"
CHAT_ID = "-1002756405394"

RSS_URL = f"https://nitter.net/{TWITTER_USER}/rss"

last_link = None

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,

import requests
import json

TELEGRAM_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send_msg(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

def check_availability():
    with open("config.json") as f:
        config = json.load(f)

    url = config["movie_url"]

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    # simple detection (can upgrade later)
    if "Buy Tickets" in response.text or "Book tickets" in response.text:
        return True

    return False


def main():
    try:
        available = check_availability()

        if available:
            send_msg("🎬 Tickets OPEN at Prasads for Avengers Endgame Encore!\nBook fast!")

        print("Checked. Available:", available)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()

from fastapi import FastAPI, Request
import requests

app = FastAPI()

# 🔐 CHANGE ONLY THESE 2 VALUES
VERIFY_TOKEN = "mytoken123"
PAGE_ACCESS_TOKEN = "EAAiIIUv6rFkBRN1qyteBlusRhTgvcEZAn7VkyVfkOik7V5ZAZAyVxYUSwbhY8qcdzwnn78gk24L4Tr8dU8ZBkyKqfZAc6xiiLEPLSMgB20FXHonwJtffofZADZC6WGnFXmWrCsknB9MiEuIo1yBdqMKH9U1qStvLfIdZAbTmYHSGQIPnZA8WStxo9uO3MWFC5QZBe0WBtWIwZDZD"


# ✅ Health Check
@app.get("/")
def home():
    return {"message": "Bot is LIVE 🚀"}


# ✅ Webhook Verification
@app.get("/webhook")
async def verify_webhook(request: Request):
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return int(challenge)

    return {"error": "Verification failed"}


# ✅ Receive Messages
@app.post("/webhook")
async def receive_message(request: Request):
    data = await request.json()

    try:
        for entry in data.get("entry", []):
            for messaging in entry.get("messaging", []):
                
                sender_id = messaging["sender"]["id"]

                if "message" in messaging and "text" in messaging["message"]:
                    user_msg = messaging["message"]["text"]

                    reply = smart_reply(user_msg)
                    send_message(sender_id, reply)

    except Exception as e:
        print("Error:", e)

    return {"status": "ok"}


# 🧠 Smart Reply Logic (EDIT THIS FOR BUSINESS)
def smart_reply(message):
    msg = message.lower()

    if "hoodie" in msg:
        return "🛍️ Black Hoodie\n💰 Price: ₹1999\n📦 Free Delivery"

    elif "hi" in msg or "hello" in msg:
        return "🙏 Namaste! Aap kya dekhna chahte ho?\n\n1️⃣ Hoodie\n2️⃣ T-shirt\n3️⃣ Offers"

    elif "price" in msg:
        return "💰 Prices start from ₹499 only!"

    else:
        return "🙏 Thanks for messaging! Hum jaldi reply karenge."


# 📤 Send Message to Instagram
def send_message(recipient_id, message_text):
    url = "https://graph.facebook.com/v18.0/me/messages"

    params = {
        "access_token": PAGE_ACCESS_TOKEN
    }

    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": message_text}
    }

    requests.post(url, params=params, json=payload)
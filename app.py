from fastapi import FastAPI
import sqlite3

app = FastAPI()

# ✅ Home route (browser test ke liye)
@app.get("/")
def home():
    return {"message": "Bot is LIVE 🚀"}

# ✅ Chat API
@app.get("/chat")
def chat(client_id: str, message: str):

    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()

    # products nikal
    cursor.execute("SELECT name, keywords, price, description FROM products WHERE client_id=?", (client_id,))
    products = cursor.fetchall()

    msg = message.lower()

    for name, keywords, price, description in products:
        keyword_list = keywords.split(",")

        for k in keyword_list:
            if k.strip() in msg:
                return {
                    "reply": f"🛍️ {name}\n💰 Price: ₹{price}\n📄 {description}"
                }

    return {"reply": "❌ Sorry, product nahi mila"}

# ✅ Webhook test (future Instagram use)
@app.get("/webhook")
def webhook():
    return {"status": "Webhook working ✅"}
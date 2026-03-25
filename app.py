from fastapi import FastAPI, Request
import sqlite3

app = FastAPI()

# =========================
# CONFIG
# =========================
VERIFY_TOKEN = "mytoken123"   # 👈 Meta webhook verify ke liye

# =========================
# HOME ROUTE
# =========================
@app.get("/")
def home():
    return {"message": "Bot is LIVE 🚀"}

# =========================
# CHAT BOT API
# =========================
@app.get("/chat")
def chat(client_id: str, message: str):

    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()

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

# =========================
# INSTAGRAM WEBHOOK VERIFY
# =========================
@app.get("/webhook")
def verify(mode: str = None, challenge: str = None, verify_token: str = None):

    if verify_token == VERIFY_TOKEN:
        return int(challenge) if challenge else "Verified"

    return "Verification failed"

# =========================
# INSTAGRAM WEBHOOK RECEIVE
# =========================
@app.post("/webhook")
async def receive_message(request: Request):

    data = await request.json()

    print("📩 Incoming:", data)

    return {"status": "received"}
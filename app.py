from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Bot is LIVE 🚀"}

@app.get("/webhook")
def webhook():
    return {"status": "working"}
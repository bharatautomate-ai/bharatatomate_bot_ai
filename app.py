from fastapi import FastAPI, Request

app = FastAPI()

VERIFY_TOKEN = "mytoken123"

@app.get("/")
def home():
    return {"message": "Bot is LIVE 🚀"}

@app.get("/webhook")
async def verify_webhook(request: Request):
    params = request.query_params

    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return int(challenge)

    return {"error": "Verification failed"}
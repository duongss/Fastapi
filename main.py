from fastapi import FastAPI
from pydantic import BaseModel
from trade_parser import parse_trade_message
from send_to_mt5 import send_order_to_mt5
import os
import uvicorn

app = FastAPI()

class Signal(BaseModel):
    text: str

@app.post("/signal")
async def receive_signal(signal: Signal):
    raw_text = signal.text
    print("📩 Nhận tín hiệu từ Telegram:", raw_text)

    trade = parse_trade_message(raw_text)
    if not trade["type"]:
        return {"status": "ignored", "message": "Không phải tín hiệu giao dịch"}

    send_order_to_mt5(trade)
    return {"status": "success", "parsed": trade}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Railway sẽ cấp PORT qua biến môi trường
    uvicorn.run("main:app", host="0.0.0.0", port=port)

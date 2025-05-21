import re

def parse_trade_message(text: str):
    """Phân tích tín hiệu từ Telegram để tách lệnh giao dịch"""
    result = {
        "type": None,       # buy/sell
        "entry": [],
        "tp": [],
        "sl": None
    }

    text = text.replace("•", " ")
    lines = text.splitlines()

    for line in lines:
        line = line.strip().lower()

        if "buy" in line or "sell" in line:
            result["type"] = "buy" if "buy" in line else "sell"
            entry_prices = re.findall(r"\d{3,5}\.?\d*", line)
            result["entry"].extend(entry_prices)

        if "tp" in line:
            tp_prices = re.findall(r"\d{3,5}\.?\d*", line)
            result["tp"].extend(tp_prices)

        if "sl" in line:
            sl_match = re.search(r"\d{3,5}\.?\d*", line)
            if sl_match:
                result["sl"] = sl_match.group()

    return result
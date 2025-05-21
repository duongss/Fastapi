import MetaTrader5 as mt5

def connect_mt5():
    login = 239581883
    password = "Dss123!@#"
    server = "Exness-MT5Trial6"

    if not mt5.initialize(login=login, password=password, server=server):
        print("Kết nối MT5 thất bại:", mt5.last_error())
        return False
    print("Kết nối MT5 thành công")
    return True

def send_order_to_mt5(trade):
    if not connect_mt5():
        return False

    symbol = "XAUUSD"
    lot = 0.1

    if trade["type"] == "buy":
        order_type = mt5.ORDER_TYPE_BUY
        price = mt5.symbol_info_tick(symbol).ask
    else:
        order_type = mt5.ORDER_TYPE_SELL
        price = mt5.symbol_info_tick(symbol).bid

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": order_type,
        "price": price,
        "deviation": 20,
        "magic": 234000,
        "comment": "Order from FastAPI",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_RETURN,
    }

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"Lệnh thất bại: {result.comment}")
        mt5.shutdown()
        return False

    print(f"Lệnh thành công: {result}")
    mt5.shutdown()
    return True

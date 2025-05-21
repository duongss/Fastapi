def send_order_to_mt5(order: dict):
    # Bạn có thể thay bằng code gửi socket hoặc ghi file JSON để Expert MT5 đọc
    print("📤 Gửi lệnh đến MT5:")
    print(f" - Kiểu: {order['type']}")
    print(f" - Entry: {order['entry']}")
    print(f" - TP: {order['tp']}")
    print(f" - SL: {order['sl']}")
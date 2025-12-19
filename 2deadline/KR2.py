def process_orders(stock_list: list[dict], orders_list: list[dict]) -> tuple[float, list[dict], list[dict]]:
    updated_stock = [item.copy() for item in stock_list]
    
    stock_dict = {item["id"]: item for item in updated_stock}
    
    total_revenue = 0.0
    canceled_orders = []
    
    for order in orders_list:
        product_id = order["id"]
        requested_count = order["count"]
        
        if product_id not in stock_dict:
            canceled_orders.append(order)
            continue
        
        product = stock_dict[product_id]
        
        if product["qty"] >= requested_count:
            product["qty"] -= requested_count
            total_revenue += product["price"] * requested_count
        else:
            canceled_orders.append(order)
    
    return total_revenue, updated_stock, canceled_orders


if __name__ == "__main__":
    stock = [
        {"id": 1, "name": "Laptop", "price": 50000, "qty": 10},
        {"id": 2, "name": "Mouse", "price": 1500, "qty": 50},
        {"id": 3, "name": "Keyboard", "price": 3000, "qty": 30},
        {"id": 4, "name": "Monitor", "price": 20000, "qty": 5}
    ]
    
    orders = [
        {"id": 1, "count": 2},
        {"id": 2, "count": 60},
        {"id": 3, "count": 10},
        {"id": 5, "count": 5},
        {"id": 4, "count": 3}
    ]
    
    revenue, new_stock, canceled = process_orders(stock, orders)
    
    print(f"Общая выручка: {revenue}")
    print("\nОбновленный склад:")
    for item in new_stock:
        print(f"  {item['name']}: {item['qty']} шт.")
    
    print("\nОтмененные заказы:")
    if canceled:
        for order in canceled:
            print(f"  Товар ID {order['id']}: запрошено {order['count']} шт.")
    else:
        print("  Нет отмененных заказов")
    
    print("\nИсходный склад:")
    for item in stock:
        print(f"  {item['name']}: {item['qty']} шт.")
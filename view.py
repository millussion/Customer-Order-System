def view_orders(orders, clients, products):
    if not orders:
        return "No orders registered."

    result = ""

    for order_id, order_data in orders.items():
        client_id = order_data[0]
        product_id = order_data[1]
        quantity = order_data[2]
        total = order_data[3]

        client_name = clients[client_id]["name"]
        product_name = products[product_id][0]

        #format the total with commas and no decimal places
        total_formatted = f"${total:,.0f}"

        result += f"""
Order ID: {order_id}
Client: {client_name}
Product: {product_name}
Quantity: {quantity}
Total: {total_formatted}
"""

    return result

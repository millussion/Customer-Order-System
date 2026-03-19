def view_orders(orders, clients, products): #receives 3 dicts

    if not orders:
        return "No orders registered." #if there are no orders return message

    result = "" #here all the info will be stored to display

    for order_id, order_data in orders.items(): #loops through each order, .items() gets both id and data
        #order_id stores the id and order_data stores the values of orders

        client_id = order_data[0] #0 because client_id is at position 0 in the tuple
        product_id = order_data[1]
        quantity = order_data[2]
        total = order_data[3]

        client_name = clients[client_id]["name"]
        product_name = products[product_id][0]
    #format the information to print
        result += f"""
Order ID: {order_id}
Client: {client_name}
Product: {product_name}
Quantity: {quantity}
Total: {total}
"""

    return result

def create_order(orders, clients, products):

    running = True
    #eto valida el id numerico
    while running:
        try:
            order_id = int(input("Enter order id: "))
            running = False
        except ValueError:
            print("Invalid order id. Only numbers.")

    #valida duplicado
    while order_id in orders:
        print("Order already exists.")
        order_id = int(input("Enter order id: "))

    #valida si el cliente ya e existente
    running = True
    while running:
        try:
            client_id = int(input("Enter client id: "))
            if client_id in clients:
                running = False
            else:
                print("Client not found.")
        except ValueError:
            print("Invalid client id.")

    #valida el producto existente
    running = True
    while running:
        try:
            product_id = int(input("Enter product id: "))
            if product_id in products:
                running = False
            else:
                print("Product not found.")
        except ValueError:
            print("Invalid product id.")

    #valida la cantida
    running = True
    while running:
        try:
            amount = int(input("Enter amount: "))
            break
        except ValueError:
            print("Invalid amount.")

    #obtiene precio del producto desde la tupla el 1 es la posicion del precio dentro de la tupla
    price = products[product_id][1]

    #calcula total
    total = price * amount

    #guarda pedido en el dic
    orders[order_id] = (client_id, product_id, amount, total)

    print("Order created successfully")

    return orders
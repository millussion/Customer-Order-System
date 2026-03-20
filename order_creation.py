
from validation import validation_id
def create_order(orders, clients, products):

    running = True
    #this validates the numeric ID
    while running:
        try:
            order_id = int(input("Enter order id: "))
            running = False
        except ValueError:
            print("Invalid order id. Only numbers.")

    #this validate if the order id is duplicate
    while order_id in orders:
        print("Order already exists.")
        order_id = int(input("Enter order id: "))


    #validate the existing client (the client have to exist/registered before to make an order)
    client_id = validation_id(clients, True)

    #validate the existing product (have to exist)
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

    #validate the amount, it have to be a int number.
    running = True
    while running:
        try:
            amount = int(input("Enter amount: "))
            running = False
        except ValueError:
            print("Invalid amount. Only numbers.")

    #gets the product price from the tuple, the 1 is the position of the price inside of the tuple.
    price = products[product_id][1]

    #calculate the total for the order, no all
    total = price * amount

    #save the order in the dictionary
    orders[order_id] = (client_id, product_id, amount, total)

    print("Order created successfully")

    return orders

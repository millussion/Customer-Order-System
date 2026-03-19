from customer_reg import * #import the function register_client(clients)
from products_registration import * #import the function register_product(products)
from order_creation import * #import the function create_order(orders, clients, products)
from view import * #import the function view_orders(orders, clients, products)
from revenue_calculation import *
# the * import everything (functions and variables)

def menu(clients, products, orders): #Dictionaries are passed as parameters to functions to avoid the use of global variables
    running = True #variable with boolean value
    while running:

        print("\n===== ORDER SYSTEM =====")
        print("1. Register client")
        print("2. Register Product")
        print("3. Create Order")
        print("4. View Order")
        print("5. Show Summary")
        print("6. Exit")

        option = input("Choose an option: ")

        if option == "1":
            clients = register_client(clients)

        elif option == "2":
            products_show = products_registration(products)
            print(f"How it is stored in the dictionary: {products_show}")

        elif option == "3":
            orders_show = create_order(orders, clients, products)
            print(f"How it is stored in the dictionary: {orders_show}")

        elif option == "4":
            info = view_orders(orders, clients, products) #Im saving the function in a variable to show it
            print(info)

        elif option == "5":
            calculation = calculate_total_sales(orders)
            print(calculation)

        elif option == "6":
            print("Exiting...")
            running = False
        
        else:
            print("Invalid option")

    return clients, products, orders 
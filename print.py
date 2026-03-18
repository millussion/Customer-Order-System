# ESTO VA EN EL MAIN
#from first import products_registration
#from three import print_products
#data = products_registration()
#print_products(data)


def print_products(products):
    print("\n=== PRODUCT LIST ===")

    # Ahora 'key' es el ID y 'value' es la tupla (name, price, amount)
    for prod_id, info in products.items():
        name, price, amount = info
        print(f"ID: {prod_id}")
        print(f"Name: {name}")
        print(f"Price: {price}")
        print(f"amount: {amount}")
        print("-------------------")


def calculate_total(products):
    total = 0
    for name, (price, amount, id) in products.items():
        total += price * amount
    return total
    
my_products= products_registration()

r_total= calculate_total(my_products)
print("=================================================")
print(f"The total revenue of the day is:{r_total}")
print("=================================================")
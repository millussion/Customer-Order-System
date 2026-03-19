def products_registration(products):
    valid = False
    while valid == False: 
        try: 
            count = int(input("Please enter the number of products you want to add: "))
            valid = True
        except ValueError:
            print ("Invalid input. Please enter a number.")
    for i in range (count):
        print(f"Product", i+1)
        name = input ("Enter the name of the product: ")

        valid = False
        while valid == False: 

            try:
                price = float (input("Enter the price of the product: "))
                valid = True
            except ValueError:
                print("Invalid inpud. Please enter a number.")


        valid = False
        while valid == False:
            try: 
               id_input = int (input ("Enter the ID of the products: "))
               if id_input in products:
                   print ("Error: this ID already exists. Please enter a different ID.")
               else: 
                   id = id_input
                   valid =True
            except ValueError: 
                print ("Invalid input. Please enter a number")


        products [id] = (name, price) 
    print("Products saved successfully")
    return products

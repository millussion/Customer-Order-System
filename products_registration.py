def products_registration(products): # Function to register products. It takes a “products” dictionary where the products will be stored.
    valid = False # Control variable for validating user input
    while valid == False: # Loop that repeats until the user enters a valid number
        try: # Attempting to convert the user's input to an integer
            count = int(input("Please enter the number of products you want to add: ")) # The user is asked how many products they want to add (count refers to the number of times)
            valid = True # If there was no error, the input is valid and the loop is exited
        except ValueError:  # If the user does not enter a number, an error message is displayed
            print ("Invalid input. Please enter a number.")
    for i in range (count): # Loop that repeats based on the specified number of items
        print(f"Product", i+1) # Displays the number of the current product. Example: The customer entered 3 in the “Quantity” field. It will display Product 1 ... Product 2...
        name = input ("Enter the name of the product: ") # Please enter the product name

        valid = False # The control variable is reset to validate the price
        while valid == False: # Loop that repeats until the entered price is valid

            try: 
                price = int(input("Enter the price of the product: ").replace (".", "").replace(",","")) # The price is requested; commas are removed before converting it to an integer (e.g., “1,000” → 1000)
                valid = True # Price valid, exits the loop
            except ValueError:
                print("Invalid inpud. Please enter a number.") # If it is not a number, an error is displayed


        valid = False # The control variable is reset to validate the ID
        while valid == False:
            try: 
               id_input = int (input ("Enter the ID of the products: ")) # Please provide the product ID
               if id_input in products: # Check that the ID is not already registered in the dictionary
                   print ("Error: this ID already exists. Please enter a different ID.") # If it already exists, request another ID
               else: 
                   id = id_input # If the ID is new, it is accepted and saved
                   valid =True # Valid ID, exit the loop
            except ValueError: 
                print ("Invalid input. Please enter a number") # If it is not a number, an error is displayed


        products [id] = (name, price) # The product is stored in the dictionary: key = ID, value = (name, price)   
    print("Products saved successfully") # Confirmation message upon completion of registration
    return products # Returns the updated dictionary containing all registered products

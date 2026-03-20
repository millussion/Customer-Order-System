def validation_id(clients, existe):
    running = True
    while running:
        try:
            client_id = int(input("Enter client id: "))

            if existe:  #exists is a boolean value created as a parameter defined in the function; so if it is true that the id exists, it validates it and moves on to the next.
                if client_id in clients:
                    return client_id
                else:
                    print("Client not found.")

            else:  #this is false; it's for registration. If it exists, it says it exists and asks again; if not, it proceeds to the next step.
                if client_id in clients:
                    print("Client already exists.")
                else:
                    return client_id

        except ValueError: 
            print("Invalid id.")

def validate_number(message):
    running = True
    while running:
        try:
            return int(input(f"Enter {message}: ")) #converts to an integer and returns to the function where it is being called
        except ValueError:
            print("Invalid input. Only numbers.")

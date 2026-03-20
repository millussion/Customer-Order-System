from validation import validation_id

def register_client(clients):
    # Ask for a client ID using a validation function.
    # The "False" means the ID should NOT already exist in the system.
    client_id = validation_id(clients, False)

    # Ask the user to enter the client's name
    name = input("Enter client name: ")

    # Ask the user to enter the client's email
    email = input("Enter client email: ")

    # Keep asking for the email until it has a basic valid format.
    # The email must contain "@" and "."
    while "@" not in email or "." not in email:
        print("Invalid email format.")
        email = input("Enter client email again: ")

    # Store the client information in the dictionary.
    # The client ID is used as the key
    clients[client_id] = {
        "name": name,
        "email": email
    }

    # Confirm that the client was added successfully
    print("Client registered successfully")

    # Return the updated clients dictionary
    return clients
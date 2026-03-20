def register_client(clients):
    client_id = validation_id(clients, False) #este booleano es lo que controla la funcion dentro de la funcion de validaciones, necesito que sea falso pq no debe existir ese id
    #pide nombre
    name = input("Enter client name: ")

    #pide email
    email = input("Enter client email: ")
    #validacion para entrar caracteres validos en el correo

    while "@" not in email or "." not in email:
      print("Invalid email format.")
      email = input("Enter client email again: ")

    clients[client_id] = { #aqui envias la informacion pedida en input
        "name": name,
        "email": email
    }

    print("Client registered successfully")

    return clients

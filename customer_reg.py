def register_client(clients):
    running = True
    #eto valida el id numerico de que no ponga letra o yqs
    while running:
        try:
            client_id = int(input("Enter client id: "))
            running = False
        except ValueError:
            print("Invalid id. Only numbers.")

    #valida si se duplica
    while client_id in clients:
        print("Client already exists.")
        client_id = int(input("Enter client id: "))
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
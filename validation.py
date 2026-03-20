def validation_id(clients, existe):
    running = True
    while running:
        try:
            client_id = int(input("Enter client id: "))

            if existe:  # existe es un valor booleano creado como parametro definido en la funcion entonces si es verdadero que el id existe lo valida y pasa al siguiente
                if client_id in clients:
                    return client_id
                else:
                    print("Client not found.")

            else:  #este es falso que es para registro, si existe dice que existe y vuelve a pedir, si no pasa al sig paso
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
            return int(input(f"Enter {message}: "))
        except ValueError:
            print("Invalid input. Only numbers.")
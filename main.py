from menu import *
# the * import everything (functions and variables)

clients = {
    101: { #these are already pre-established clients
        "name": "Ana Pérez",
        "email": "ana@email.com"
    },
    102: {
        "name": "Ronald Pérez",
        "email": "ronald@email.com"
    }
}
products = {
    999: ("Arroz", 5000), #these are already pre-established products
    933: ("Coco", 2000),
    929: ("Chocolate", 3000)
}
orders = {

}

menu(clients, products, orders) #Dictionaries are passed as parameters to functions to avoid the use of global variables

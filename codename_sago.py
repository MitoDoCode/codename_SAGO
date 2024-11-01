import json
import os

USER_DATA_FILE = 'slaves.json'
ROOMS_DATA_FILE = 'rooms.json'

def load_users():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

def load_rooms():
    if os.path.exists(ROOMS_DATA_FILE):
        with open(ROOMS_DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

def room_name(room, about_room, price):
    
    if room in rooms:
        return "Room already exists."
    else:
        rooms[room] = {"description": about_room, "price": price}
        save_rooms(rooms)
        return "Room added successfully!"

def save_users(users):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(users, file)

def save_rooms(rooms):
    with open(ROOMS_DATA_FILE, 'w') as file:
        json.dump(rooms, file)

slaves = load_users()
rooms = load_rooms()

def register(username, password):
    if username in slaves:
        return "Username already exists!"
    else:
        slaves[username] = password
        save_users(slaves)
        return "Registration successful!"

def login(username, password):
    if username in slaves:
        if slaves[username] == password:
            return f"Welcome, {username}!"
        else:
            return "Incorrect password!"
    else:
        return "User not found!"

def view_users():
    return slaves.keys()

sago_art = [
    "|-------------------------------------|",
    "|  #####    ####    #####   #######   |",
    "| #     #  #     # #     #  #     #   |",
    "| #        #     # #        #     #   |",
    "|  #####   ####### #  ####  #     #   |",
    "|       #  #     # #     #  #     #   |",
    "| #     #  #     # #     #  #     #   |",
    "|  #####   #     #  #####   #######   |",
    "|    S O M A N Y | S O Y U M M Y      |",
    "|-------------------------------------|",
]

MainMenu = [
    "WELCOME TO SAGO HOW CAN WE HELP YOU",
    "----------1.LOGIN------------------",
    "----------2.SIGNUP-----------------",
    "----------3.ROOMS------------------",
]

while True:
    for line in sago_art:
        print(line)

    for guhit in MainMenu:
        print(guhit)

    number = input("Enter a number (1, 2, or 3): ")

    if number.isdigit():
        number = int(number)

    if number == 1:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        print(login(username, password))

    elif number == 2:
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        print(register(username, password))

    elif number == 3:
        print(f"You selected {number}: ROOMS")

    elif number == 6996:
        print("ADMIN ROOM CONSOLE")
        room = input("Enter a Room Name: ")
        about_room = input("What is this room: ")

        while True:
            try:
                price = float(input("Enter room price: "))
                break
            except ValueError:
                print("Invalid price. Please enter a numeric value.")

        print(room_name(room, about_room, price))

    else:
        print("INVALID NUMBER")

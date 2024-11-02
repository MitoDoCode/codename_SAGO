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

def room_name(room, about_room, price, size):
    if room in rooms:
        return ">>>>>Room already exists.<<<<<"
    else:
        rooms[room] = {"description": about_room, "price": price, "size": size}
        save_rooms(rooms)
        return ">>>>>Room added successfully!<<<<<"

def save_users(users):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(users, file)

def save_rooms(rooms):
    with open(ROOMS_DATA_FILE, 'w') as file:
        json.dump(rooms, file)

def display_rooms(size_filter=None):
    rooms_data = load_rooms()
    if rooms_data:
        print("Rooms Data:")
        for room_name, details in rooms_data.items():
            if size_filter is None or details['size'] == size_filter:
                print("---------------------------------------")
                print(f"Room: {room_name}")
                print(f"  Description: {details['description']}")
                print(f"  Price: {details['price']}")
                print(f"  Size: {details['size']}")
                print("---------------------------------------")
    else:
        print("No room data found in rooms.json.")

slaves = load_users()
rooms = load_rooms()

def register(username, password):
    if username in slaves:
        return ">>>>>Username already exists!<<<<<"
    else:
        slaves[username] = password
        save_users(slaves)
        return ">>>>>Registration successful!<<<<<"

def login(username, password):
    if username in slaves:
        if slaves[username] == password:
            return f"Welcome, {username}!"
        else:
            return ">>>>>Incorrect password!<<<<<"
    else:
        return ">>>>>User not found!<<<<<"

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

SubMenu = ["1. RESERVE A ROOM", "2. LOGOUT"]

RoomsizeMenu = ["Small Room", "Medium Room", "Large Room"]

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
        login_result = login(username, password)
        print(login_result)
        
        if "Welcome" in login_result:
            while True:
                print("\nSubmenu:")
                for option in SubMenu:
                    print(option)

                sub_choice = input("Enter a choice (1 or 2): ")
                
                if sub_choice == "1":
                    print("Room reservation")
                    
                   
                    print("Select room size:")
                    for i, size_option in enumerate(RoomsizeMenu, start=1):
                        print(f"{i}. {size_option}")

                    size_choice = input("Enter the number of the size you want: ")
                    if size_choice.isdigit() and 1 <= int(size_choice) <= len(RoomsizeMenu):
                        selected_size = RoomsizeMenu[int(size_choice) - 1]
                        display_rooms(size_filter=selected_size)
                    else:
                        print(">>>>>INVALID SIZE CHOICE<<<<<")
                
                elif sub_choice == "2":
                    print("Log Out")
                    break
                
                else:
                    print(">>>>>INVALID CHOICE<<<<<")
                    
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
                print(">>>>>Invalid price. Please enter a valid number.<<<<<")
        
        print("Select room size:")
        for i, size_option in enumerate(RoomsizeMenu, start=1):
            print(f"{i}. {size_option}")
        
        size_choice = input("Enter the number of the size you want: ")
        if size_choice.isdigit() and 1 <= int(size_choice) <= len(RoomsizeMenu):
            selected_size = RoomsizeMenu[int(size_choice) - 1]
            print(room_name(room, about_room, price, selected_size))
        else:
            print(">>>>>INVALID SIZE CHOICE<<<<<")

    else:
        print(">>>>>INVALID NUMBER<<<<<")

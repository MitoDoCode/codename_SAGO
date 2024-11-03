import json
import os
from datetime import datetime

USER_DATA_FILE = 'slaves.json'
ROOMS_DATA_FILE = 'rooms.json'
RESERVED_ROOMS_DATA_FILE = 'reservedrooms.json'


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
    "----------3.?????------------------",
]

SubMenu = [
    "1. RESERVE A ROOM",
    "2. VIEW MY RESERVED ROOMS",
    "3. DELETE MY RESERVED ROOM",
    "4. LOGOUT"
]

RoomsizeMenu = ["Small Room", "Medium Room", "Large Room"]

START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2024, 12, 31)
MAX_RESERVATION_DAYS = 30


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

def load_reserved_rooms():
    if os.path.exists(RESERVED_ROOMS_DATA_FILE):
        with open(RESERVED_ROOMS_DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_reserved_rooms(reserved_rooms):
    with open(RESERVED_ROOMS_DATA_FILE, 'w') as file:
        json.dump(reserved_rooms, file)

def save_users(users):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(users, file)

def save_rooms(rooms):
    with open(ROOMS_DATA_FILE, 'w') as file:
        json.dump(rooms, file)

def is_valid_date_range(check_in, check_out):
    try:
       
        check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
        check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
       
        if not (START_DATE <= check_in_date <= END_DATE) or not (START_DATE <= check_out_date <= END_DATE):
            print(">>>>>Reservation dates must be between 2024-01-01 and 2024-12-31.<<<<<")
            return False

        if check_out_date <= check_in_date:
            print(">>>>>Check-out date must be after check-in date.<<<<<")
            return False

        reservation_length = (check_out_date - check_in_date).days
        if reservation_length > MAX_RESERVATION_DAYS:
            print(f">>>>>Reservation cannot exceed {MAX_RESERVATION_DAYS} days.<<<<<")
            return False

        return True
    except ValueError:
        print(">>>>>Invalid date format. Please enter dates in YYYY-MM-DD format.<<<<<")
        return False
 
def delete_user_reserved_room(username):
    reserved_rooms = load_reserved_rooms()
    user_rooms = reserved_rooms.get(username, {})

    if not user_rooms:
        print(f"No rooms reserved by {username} to delete.")
        return

    print("Your Reserved Rooms:")
    for room_name in user_rooms.keys():
        print(f"- {room_name}")

    room_to_delete = input("Enter the name of the room you want to delete: ")
    if room_to_delete in user_rooms:
        del user_rooms[room_to_delete]
        if not user_rooms:  
            del reserved_rooms[username]
        save_reserved_rooms(reserved_rooms)
        print(f">>>>>Room '{room_to_delete}' has been deleted from your reservations!<<<<<")
    else:
        print(">>>>>Room not found in your reserved rooms!<<<<<")    
    
def display_rooms(size_filter=None):
    rooms_data = load_rooms()
    available_rooms = []
    if rooms_data:
        for room_name, details in rooms_data.items():
            if size_filter is None or details['size'] == size_filter:
                print("---------------------------------------")
                print(f"Room: {room_name}")
                print(f"  Description: {details['description']}")
                print(f"  Price: {details['price']}")
                print(f"  Size: {details['size']}")
                available_rooms.append(room_name)
                print("---------------------------------------")
    else:
        print("No room data found in rooms.json.")
    return available_rooms

def reserve_room(username, room_name, check_in, check_out):
    reserved_rooms = load_reserved_rooms()
    reservation_code = generate_reservation_code()
    if username not in reserved_rooms:
        reserved_rooms[username] = {}

    if room_name in reserved_rooms[username]:
        print(">>>>>Room is already reserved.<<<<<")
    else:
        reserved_rooms[username][room_name] = {"check_in": check_in, "check_out": check_out, "reservation_code": reservation_code}
        save_reserved_rooms(reserved_rooms)
        print(f">>>>>Room '{room_name}' reserved successfully from {check_in} to {check_out}. Your reservation code is {reservation_code}.<<<<<")

def view_user_reserved_rooms(username):
    reserved_rooms = load_reserved_rooms()
    user_rooms = reserved_rooms.get(username, {})

    if user_rooms:
        print(f"\nReserved Rooms for {username}:")
        for room_name, details in user_rooms.items():
            print("---------------------------------------")
            print(f"Room: {room_name}")
            print(f"  Check-in Date: {details['check_in']}")
            print(f"  Check-out Date: {details['check_out']}")
            print(f"  Reservation Code: {details['reservation_code']}")
            print("---------------------------------------")
    else:
        print(f"No rooms reserved by {username}.")

def register(username, password):
    slaves = load_users()
    if username in slaves:
        return ">>>>>Username already exists!<<<<<"
    else:
        slaves[username] = password
        save_users(slaves)
        return ">>>>>Registration successful!<<<<<"

def login(username, password):
    slaves = load_users()
    if username in slaves:
        if slaves[username] == password:
            return f"Welcome, {username}!"
        else:
            return ">>>>>Incorrect password!<<<<<"
    else:
        return ">>>>>User not found!<<<<<"

def generate_reservation_code():
    from random import randint
    return str(randint(100000, 999999))

def display_all_rooms():
    rooms_data = load_rooms()
    if rooms_data:
        print("All Available Rooms:")
        for room_name, details in rooms_data.items():
            print("---------------------------------------")
            print(f"Room: {room_name}")
            print(f"  Description: {details['description']}")
            print(f"  Price: {details['price']}")
            print(f"  Size: {details['size']}")
            print("---------------------------------------")
    else:
        print("No room data found in rooms.json.")

def admin_room_console():
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
        add_room(room, about_room, price, selected_size)
    else:
        print(">>>>>INVALID SIZE CHOICE<<<<<")

def add_room(name, description, price, size):
    rooms = load_rooms()
    rooms[name] = {
        "description": description,
        "price": price,
        "size": size
    }
    save_rooms(rooms)
    print(f">>>>>Room '{name}' added successfully!<<<<<")

def main_menu():
    while True:
        for line in sago_art:
            print(line)
        for guhit in MainMenu:
            print(guhit)

        number = input("Enter a number (1 or 2): ")

        if number == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            login_result = login(username, password)
            print(login_result)

            if "Welcome" in login_result:
                sub_menu(username)
        elif number == "2":
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            print(register(username, password))
        elif number == "Three":
            print("MONIKA:>6996 ADMIN CONSOLE")
        elif number == "6996":
            admin_room_console()
        else:
            print(">>>>>INVALID CHOICE<<<<<")

def sub_menu(username):
    while True:
        print("\nSubmenu:")
        for option in SubMenu:
            print(option)

        sub_choice = input("Enter a choice (1, 2, 3, or 4): ")

        if sub_choice == "1":
            print("Room reservation")
            print("Select room size:")
            for i, size_option in enumerate(RoomsizeMenu, start=1):
                print(f"{i}. {size_option}")

            size_choice = input("Enter the number of the size you want: ")
            if size_choice.isdigit() and 1 <= int(size_choice) <= len(RoomsizeMenu):
                selected_size = RoomsizeMenu[int(size_choice) - 1]
                available_rooms = display_rooms(size_filter=selected_size)

                if available_rooms:
                    room_choice = input("Enter the name of the room you want to reserve: ")
                    if room_choice in available_rooms:
                        check_in = input("Enter check-in date (YYYY-MM-DD): ")
                        check_out = input("Enter check-out date (YYYY-MM-DD): ")
                        reserve_room(username, room_choice, check_in, check_out)
                    else:
                        print(">>>>>INVALID ROOM CHOICE<<<<<")
                else:
                    print(">>>>>No rooms available for selected size.<<<<<")
            else:
                print(">>>>>INVALID SIZE CHOICE<<<<<")

        elif sub_choice == "2":
            view_user_reserved_rooms(username)

        elif sub_choice == "3":
            delete_user_reserved_room(username)  
        elif sub_choice == "4":
            print("Log Out")
            break

        else:
            print(">>>>>INVALID CHOICE<<<<<")
            
main_menu()

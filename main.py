import RoomClass as R

rooms = {1: {"name": "Start", "Contains": [1, 2], "Connects": [2, 3]},
         2: {"name": "Start1", "Contains": [3, 4], "Connects": [1, 2]},
         3: {"name": "Start2", "Contains": [5, 6], "Connects": [1]}
         }


def room_gen():
    print("Please enter the name of the room: ")
    name = input()
    id_connect_list = []
    id_contains_list = []
    if rooms:
        print("List of rooms that you can connect to: ")
        for key in rooms.keys():
            print("Name of room: '", rooms[key]["name"], "' Contains of the room: ", rooms[key]["Contains"],
                  " Connections to/from of the room: ", rooms[key]["Connects"])
        while True:
            print(
                "Please provide the id of the room that you want to connect to, if you want to stop adding connections write 0: ")
            id_connect = input()
            if id_connect.isdecimal():
                if int(id_connect) != 0:
                    id_connect_list.append(int(id_connect)) #Do zmiany
                if int(id_connect) == 0:
                    break
        while True:
            print(
                "Please provide the id of the contains that should appear in the room, if you want to stop adding connections write 0: ")
            id_contains = input()
            if id_contains.isdecimal():
                if int(id_contains) != 0:
                    id_contains_list.append(int(id_contains)) #Do zmiany
                if int(id_contains) == 0:
                    break
        id_of_room = list(rooms.keys())[-1] + 1
        rooms[id_of_room] = {"name": name, "Contains": id_contains_list, "Connects": id_connect_list}
        print(rooms)

def main():
    rooms = {
        1: {"name": "", "Contains": [], "Connects": []}
    }
    name = input()

    rooms[2] = {"name": name, "Contains": [1], "Connects": [3]}

    print(rooms.keys())


if __name__ == '__main__':
    room_gen()

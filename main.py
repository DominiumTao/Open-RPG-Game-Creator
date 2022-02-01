import RoomClass as R

rooms = {
}


def room_gen():
    id_connect_list = []
    id_contains_list = []
    rooms_temp = {}

    def add_conn(rooms_temp):
        rooms.update(rooms_temp)

    def contains_gen():
        id_contains_list_in = []
        while True:
            print(
                "Please provide the id of the contains that should appear in the room, if you want to stop adding connections write 0: ")
            id_contains = input()
            if id_contains.isdecimal():
                if int(id_contains) != 0:
                    id_contains_list_in.append(int(id_contains))  # Do zmiany
                if int(id_contains) == 0:
                    return id_contains_list_in

    print("Please enter the name of the room: ")
    name = input()
    if rooms:
        print("List of rooms that you can connect to: ")
        for key in rooms.keys():
            print("ID of room: ", key, "Name of room: '", rooms[key]["name"], "' Contains of the room: ",
                  rooms[key]["Contains"],
                  " Connections to/from of the room: ", rooms[key]["Connects"])
        while True:
            print(
                "Please provide the id of the room that you want to connect to, if you want to stop adding connections write 0: ")
            id_connect = input()
            if id_connect.isdecimal():
                if int(id_connect) != 0:
                    id_connect_list.append(int(id_connect))  # Do zmiany
                if int(id_connect) == 0:
                    break
        id_contains_list = contains_gen()
        id_of_room = list(rooms.keys())[-1] + 1
        rooms_temp[id_of_room] = {"name": name, "Contains": id_contains_list, "Connects": id_connect_list}
        add_conn(rooms_temp)
    else:
        print("**GENERATING FIRST ROOM**")
        id_contains_list = contains_gen()
        rooms_temp[1] = {"name": name, "Contains": id_contains_list, "Connects": id_connect_list}
        add_conn(rooms_temp)


def main():
    rooms = {
        1: {"name": "", "Contains": [], "Connects": []}
    }
    name = input()

    rooms[2] = {"name": name, "Contains": [1], "Connects": [3]}

    print(rooms.keys())


if __name__ == '__main__':
    room_gen()
    print(rooms)

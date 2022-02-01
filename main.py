import RoomClass as R

rooms = {1: {'name': 'Startowa_Lokacja', 'Contains': [1, 2], 'Connects': [2]}
         }


def room_gen():
    id_connect_list = []
    id_contains_list = []
    rooms_temp = {}

    def add_conn(rooms_temp, bool):
        if bool:
            temp_dic = rooms_temp[list(rooms_temp.keys())[0]]
            conn = temp_dic["Connects"]
            for e_conn in conn:
                if not list(rooms_temp.keys())[0] in rooms[e_conn]["Connects"]:
                    rooms[e_conn]["Connects"].append(list(rooms_temp.keys())[0])
                    print(rooms[e_conn], "tu")
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
        add_conn(rooms_temp, True)
    else:
        print("**GENERATING FIRST ROOM**")
        id_contains_list = contains_gen()
        rooms_temp[1] = {"name": name, "Contains": id_contains_list, "Connects": id_connect_list}
        add_conn(rooms_temp, False)


def containers_config():
    while True:
        for key in rooms.keys():
            print("ID of room: ", key, "Name of room: '", rooms[key]["name"], "' Contains of the room: ",
                  rooms[key]["Contains"],
                  " Connections to/from of the room: ", rooms[key]["Connects"])
        print(f"Please provide room id that you want want to config, if you don't want to config any containers please enter 0:  ")
        room_id = input()
        # room_id = int(room_id)
        if room_id.isdecimal() and int(room_id) in rooms.keys() and int(room_id) != 0:
            print("s")
        elif room_id.isdecimal() and int(room_id) == 0:
            break
        else:
            print("\nPlease enter only id number example '1', without apostrophe, check if number is correct ID number\n\n" )

def main():
    # room_gen()
    containers_config()


if __name__ == '__main__':
    main()

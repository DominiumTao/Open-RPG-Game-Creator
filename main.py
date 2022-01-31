import RoomClass as R


def main():
    rooms = {
        1: {"name": "", "Contains": [], "Connects": []}
    }
    name = input()

    rooms[2] = {"name": name, "Contains": [1], "Connects": [3]}

    print(rooms)


if __name__ == '__main__':
    main()
    print("koniec")

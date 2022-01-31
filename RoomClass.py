class Room():
    Id = None
    Contains = None
    Connections = None
    def __init__(self, id, contains, connections):
        self.Id = id
        self.Contains = contains
        self.Connections = connections
    def __str__(self):
        print(f"Id - must be an unique number in all of Room classes"
              f"Contains -  Id's of items that room will contain"
              f"Connections - Id's of another Room's an unique number specified in __init__ as first variable.")


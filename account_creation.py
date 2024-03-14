
def login(database, username, password):
        if username in database and database[username] == password:
            print(f"Welcome back {username} to WordJumble!")
            return username
        elif username in database and database[username] != password:
            print("Incorrect password.")
            return ""
        else:
          print("User not found. Please register. Please register")
          return ""

def register(database, username, password):
    if username in database:
        print(f"Username {username} already registered.")
        return ""
    elif username not in database:
        database[username] = password
        print(database)
        print(f"{username} has been registered.")
        print("Welcome to WordJumble!")
        return username

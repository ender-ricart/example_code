def login(database, username, password):
        if username in database and database[username] == password:
            print(f"Welcome back {username}!")
            return username
        elif username in database and database[username] != password:
            print("Incorrect password for admin.")
            return ""
        else:
          print("User not found. Please register.")
          return ""

def register(database, username):
    if username in database:
        print(f"Username {username} already registered.")
        return ""
    else:
        print(f"The username - {username} - has been registered.")
        return username
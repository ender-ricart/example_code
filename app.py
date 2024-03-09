#imports
from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register
#variables
database = {"admin":"password123"}
donations = []
authorized_user = ""
#code

while True:
    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print(f"Logged in as: {authorized_user}.")
    choose_option = (input("Input your selection from the DonateMe Homepage:  ")).lower()
    if choose_option == "1" or choose_option == "login":
        username = input("Please enter your username:  ")
        password = input("Please enter your password:  ")
        authorized_user =login(database, username, password)
        
    elif choose_option == "2" or choose_option == "register":
        username = input("Please enter your username:  ")
        password = input("Please enter your password:  ")
        authorized_user =register(database, username)
        if authorized_user != "":
            database[username] = password
            print('DEBUG:', database)

    elif choose_option == "3" or choose_option == "donate":
        if authorized_user == "":
            print("You are not logged in.")
        if authorized_user != "":
            donations.append(donate(username))
        else:
            print("Please enter a valid number.")
    elif choose_option == "4" or choose_option == "show donations":
        show_donations(donations)        
    elif choose_option == "5" or choose_option == "exit":
        print("Goodbye.")
        #log out
        authorized_user = ""
        #to return to homepage
        continue
    else:
        print("Please select an option from the homepage.")

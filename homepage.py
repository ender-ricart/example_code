#DonateMe

def show_homepage():
    print("""
         === DonateMe Homepage ===
    -------------------------------------
    |1. Login       | 2. Register       |
    -------------------------------------  
    |3. Donate      | 4. Show Donations |
    -------------------------------------  
    |             5. Exit               |
    -------------------------------------  
 """)
    
def donate(username):
    donation_amount = input("How much would you like to donate? ")
    if donation_amount.isdigit() or float(donation_amount):
        donation_string = f"{username} donated ${donation_amount}"
        return donation_string
    else:
        print("Please enter a valid number. Do not include commas.")

def show_donations(donations):
    if len(donations) == 0:
        print("There are no donations.")

    else:
        total_donations = 0.0
        print("--- All Donations ---")
        for donation in donations:
            print(donation)




    
    
    
# P3LAB_PenuelNathanael.py
# This program will tell the user the most effecient change

def calculate_change(amount):
    # Convert the amount to an integer
    cents = int(round(amount * 100))

    # Number of dollars
    dollars = cents // 100
    cents %= 100

    # Mumber of quarters
    quarters = cents // 25
    cents %= 25

    # Number of dimes
    dimes = cents // 10
    cents %= 10

    # Number of nickels
    nickels = cents // 5
    cents %= 5

    # Remaining cents are pennies
    pennies = cents

    # Display the results
    if dollars:
        print(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    if quarters:
        print(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if dimes:
        print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if nickels:
        print(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if pennies:
        print(f"{pennies} Penn{'ies' if pennies > 1 else 'y'}")
    if not (dollars or quarters or dimes or nickels or pennies):
        print("No change")

# Main program
try:
    amount = float(input("Enter the amount of money as a float: $"))
    calculate_change(amount)
except ValueError:
    print("Invalid input. Please enter a valid float number.")

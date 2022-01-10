"""
Name: Jillian Landin
hw1.py

Problem: Interact with simple Python programs that produce output and do arithmetic.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area = ", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume = ", volume)


def shooting_percentage():
    total_shots = eval(input("Enter the player's total shots: "))
    shots_made = eval(input("Enter how many shots the player made: "))
    percentage = (shots_made / total_shots) * 100
    print("Shooting Percentage = ", percentage, "%")


def coffee():
    pounds_coffee = eval(input("How many pounds of coffee would you like?"))
    total_cost = pounds_coffee * (10.50 + .86) + 1.50
    print("Your total is: ", round(total_cost, 2))


def kilometers_to_miles():
    km_traveled = eval(input("How many kilometers did you travel?"))
    miles = km_traveled / 1.61
    print("That's", miles, "miles!")


if __name__ == '__main__':
    pass

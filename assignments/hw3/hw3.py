"""
Name: Jillian Landin
hw3.py

Problem: determining averages with for loops

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""


def average():
    number_inputs = eval(input("how many grades will you enter?"))
    acc = 0
    for _ in range(number_inputs):
        grades = eval(input("enter grade"))
        acc = acc + grades
    mean = acc / number_inputs
    print("Average = ", mean)


def tip_jar():
    acc = 0
    for _ in range(5):
        tips = eval(input("Enter your tip:"))
        acc = acc + tips
    print("Total tips: $", acc)


def newton():
    number = eval(input("what number do you want to square root?"))
    approx = eval(input("how many times should we improve the approximation?"))
    root = 0
    for i in range(1, approx):
        root = (number / i) / 2
        root += (root / 2)
    print(root)


def sequence():
    terms = eval(input("Enter the number of terms you want:"))
    for i in range(0, terms):
        acc = i + (i + 1) % 2
        print(acc, end=" ")


def pi():
    num_terms = eval(input("Enter the number of terms you wish to use for approximation:"))
    acc = 4
    for i in range(1, num_terms + 1):
        num = i + (i + 2) % 2
        denom = i + (i + 1) % 2
        acc = acc * (num / denom)
    print(acc / 2)


if __name__ == '__main__':
    pass

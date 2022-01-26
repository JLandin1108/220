"""
Name: Jillian Landin
hw2.py

Problem: practicing loops with brief arithmetic

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    upper_bound = eval(input("Enter upper bound value:"))
    acc = 0
    for i in range(0, upper_bound + 1, 3):
        acc = acc + i
    print(acc)


def multiplication_table():
    for i in range(1, 11):
        for num in range(1, 11):
            print(i * num, end=" ")
        print()


def triangle_area():
    side_a = eval(input("Enter side a:"))
    side_b = eval(input("Enter side b:"))
    side_c = eval(input("Enter side c:"))
    equation_one = (side_a + side_b + side_c) / 2
    equation_two = equation_one * (equation_one - side_a) * (equation_one - side_b)\
                   * (equation_one - side_c)
    area = math.sqrt(equation_two)
    print("Area = ", area, "units")


def sum_squares():
    lower_bound = eval(input("Enter lower bound value:"))
    upper_bound = eval(input("Enter upper bound value:"))
    acc = 0
    for i in range(lower_bound, upper_bound + 1):
        acc = acc + i ** 2
    print(acc)


def power():
    base = eval(input("Enter your base value:"))
    exponent = eval(input("Enter your exponent value:"))
    acc = 1
    for _ in range(exponent):
        acc = acc * base
    print(base, "^", exponent, "=", acc)


if __name__ == '__main__':
    pass

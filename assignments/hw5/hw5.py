"""
Name: Jillian Landin
hw5.py

Problem: reordering and changing strings

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    name = input("Print first and last name:").split()
    first = name[0]
    last = name[1]
    print(last + ", " + first)


def company_name():
    web = input("Enter your domain name:").split(".")
    name = web[1]
    print(name)


def initials():
    num_names = eval(input("How many students are in the class?"))
    for i in range(num_names):
        name = input("what is the name of student " + str(i + 1) + "?")
        string = name.split(" ")
        first = string[0]
        last = string[1]
        print(first[0] + last[0])


def names():
    group_names = input("enter a list of names:").split(", ")
    for i in group_names:
        name = i.split(" ")
        first = name[0]
        last = name[1]
        init = first[0] + last[0]
        print(init, end=" ")


def thirds():
    num_sentences = eval(input("enter the number of sentences:"))
    acc = []
    for i in range(num_sentences):
        sentence = (input("Sentence " + str(i + 1) + ":"))
        threes = sentence[::3]
        acc.append(threes)
    print(acc)


def word_average():
    sentence = input("enter a sentence:")
    words = sentence.split()
    num_words = len(words)
    acc = 0
    for word in words:
        num_letters = len(word)
        acc += num_letters
    print(acc / num_words)


def pig_latin():
    sentence = input("Sentence to convert to pig latin:").split(" ")
    translation = ''
    for word in sentence:
        pig = word[1:] + word[0] + "ay" + " "
        translation += pig.lower()
    print(translation[:-1])


if __name__ == '__main__':
    pass

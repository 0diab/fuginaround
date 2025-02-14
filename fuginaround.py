# s = input("sammys: ")
# m = input("sammys: ")
# l = input("sammys: ")
# xl = input("sammys: ")
#
# x = 10.55
# mins = 0
# print(x)
# vv = str(x).split('.')
# a, b = int(vv[0]), int(vv[1])
# print(a+b)
#
# for i in range(int(x)):
#     x -= 1
#     mins += 1
# print(f"{mins} minutes {int(x * 60)} seconds")


# for i in range(int(x)):
#     x -= 1
#     mins += 1
# print(f"{mins} minutes {int(x * 60)} seconds")


# usr = int(input("what is the length of one side? "))
# def areaSquare(square):
#     area = square * square
#     return area
#
# usr = int(input("what is the length of one side? "))
# def areaSquare(square):
#     area = square * square
#     return area
#
# squareArea = areaSquare(usr)
# print(f"The area of the square is {squareArea}")

#
# def ohmslawV(ohm,I):
#     v = ohm * I
#     return v
# current = float(input("what is the current? "))
# resistance = float(input("what is the resistance? "))
#
# voltage =  ohmslawV(resistance,current)
# print(f"The voltage is {voltage:.2f}")
#
#
# def ohmslawR(v,I):
#     R = v/I
#     return R
# voltage = float(input(f"what is the voltage? "))
# current = float(input(f"what is the current? "))
#
# resistance = ohmslawR(voltage,current)
# print(f"The resistors value is {resistance:.2f}")
#


# x = float(input(f"what is your grade "))
# if x > 100 or x < 0:
#     input("That is not a valid grade, input your real grade ")
# if x >= 89.5:
#     print(f"your grade is an A")
# elif x >= 79.5:
#     print(f"your grade is a B")
# elif x > 69.5:
#     print(f"your grade is a C")
# else:
#     print(f"Not good")

#
# boomMeter = int(input(f"How many BOOMS does the DOUBLE CHUNK CHOCOLATE COOOKIE get on the BOOM meter? "))
# match boomMeter:
#     case 0:
#         print(f"DOOOOOOOOOM")
#     case 1:
#         print(f"BOOM")
#     case 2:
#         print((f"BOOOOM, BOOOOM"))
#     case 3:
#         print(f"BOOOM, BOOOOM, BOOOOOOOOOOOM")
#     case 4 :
#         print(f"BOOOM, BOOOOM, BOOOOOM, BOOOOOOOOOOOOOOM")
#     case 5:
#         print(f"FIVE BIIIIG BOOOMS! BOOOOOOOOOOOM, BOOOOOOOOOOOOOOM, BOOOOOOOOOOOM, BOOOOOOOOOOM, BOOOOOOOOOOOOOOOOOOOOOOOM!!!!")
#     case _:
#         print(f"DOOOOOOOOOOM")



# r = float(input(f"what is the radius of your circle?"))
# def area(raidus):
#     areaC = 3.14*raidus*raidus
#     print(f"The area of your circle is {areaC:0.2f}")
#     return areaC
#
# area(r)
#


# Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
# firstName = input("What is your first name? ")
# lastName = input("What is your last name?")
#
# def reverse(a,b):
#     switch = print(f"{b} {a}")
#     return switch
# reverse(firstName,lastName)
#
# colors = ["red", "blue" , "green", "black"]
# print(f"{colors[0]}, {colors[-1]}")

# examDate = input("what date is your exam? ")
# vv = str(examDate).split("/")
# day , month , year = (vv[0]),(vv[1]),(vv[2])
# print(f"exam is on {day}/{month}/{year}")


# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615
# num = int(input("choose a random number: "))
#
# def convert(input1):
#     new1 = f"{input1}"
#     new2 = f"{input1}{input1}"
#     new3 = f"{input1}{input1}{input1}"
#     sum1 = int(new1)+int(new2)+int(new3)
#     print(f"{sum1}")
#     return sum1
#
# convert(num)

# Write a Python program to get the volume of a sphere with radius six.
# from math import pi
#
# def SphereV(r):
#     # pie = 3.14
#     volume = (4/3)*pi*r**3
#     print(f"the volume of your sphere is {volume:.2f}")
#     return volume
# raidus = float(input(f"what is the radius of your sphere?\n"))
# SphereV(raidus)

# Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.

# def diff(input):
#     n = input - 17
#     if n > 17:
#         n1 = n*2
#         print(f"{n1}")
#     return n
#
# nomber = int(input("nomber pls: "))
# diff(nomber)



# Write a Python program to test whether a number is within 100 of 1000 or 2000.
# noomb = int(input("typer a number"))
# if noomb > 899 and noomb < 1101:
#     print(f"your number is within 100 of 1000")
# elif noomb > 1899 and noomb <2101:
#     print(f"your numer is within 100 of 2000")
# else
#     print(f"your number is not within 100 of both 1000 and 2000")

# https://www.w3resource.com/python-exercises/python-basic-exercises.php1



# Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
# input1 = int(input("random number 1: "))
# input2 = int(input("random number 2: "))
# input3 = int(input("random number 3: "))
#
#
# if input1 == input2 == input3:
#     print(3*(input1+input2+input3))
# else:
#     print(input1+input2+input3)



# Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front.
# Return the string unchanged if the given string already begins with "Is".

# question = input(f"what is your question?")
# phrase = "Is"
# position = 0
#
# if question.find(phrase,position) == position:
#     print(f"{question}")
# else:
#     print(f"Is {question}")


# Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
# x = float(input("nomber: "))
# y = x % 2
#
# if y > 0:
#     print("odd")
# else:
#     print("even")


# alphabet = input("Enter a letter: ")
# #
# # if alphabet == "a" or alphabet == "e" or alphabet == "i" or alphabet == "o" or alphabet == "u":
# # # if alphabet == "aeiou":
# #     print("your letter is a vowel")
# # else:
# #     print("your letter is not a vowel :(")

# for num in range(11,55,2):
#     if num != 0:
#         print(num)


# mult = int(input("enter a number:"))
#
# for multiplication in range (-2,11):
#     result = mult * multiplication
#     print(result)

# result = 1 % 2
#
# if result == 0:
#
#     print("TRUE")
#
# else:
#     print("FALSE")


# Create a program that allows the user to guess a secret number between 1 and 100. The program should keep prompting the user until they guess the correct number.
# from random import randint
# secretNum = randint(1,100)
# print(secretNum)
#
# guess = int(input("Guess a number between 1 and 100: "))
#
# while guess != secretNum:
#     print("Wrong number :(")
#     guess = int(input("guess again: "))
#
# print("you guessed correctly :)")

# for row in range (1,11):
#     for col in range (row):
#         print("* ", end="")
#     print()


# n = True
# for number in range(1,4,n):
#     dot = "."*(number)
#     print(f"attempt {number}, {dot} ")
#     if n:
#         print("success")


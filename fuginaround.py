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


boomMeter = int(input(f"How many BOOMS does the DOUBLE CHUNK CHOCOLATE COOOKIE get on the BOOM meter? "))

match boomMeter:
    case 0:
        print(f"DOOOOOOOOOM")
    case 1:
        print(f"BOOM")
    case 2:
        print((f"BOOOOM, BOOOOM"))
    case 3:
        print(f"BOOOM, BOOOOM, BOOOOOOOOOOOM")
    case 4 :
        print(f"BOOOM, BOOOOM, BOOOOOM, BOOOOOOOOOOOOOOM")
    case 5:
        print(f"FIVE BIIIIG BOOOMS! BOOOOOOOOOOOM, BOOOOOOOOOOOOOOM, BOOOOOOOOOOOM, BOOOOOOOOOOM, BOOOOOOOOOOOOOOOOOOOOOOOM!!!!")
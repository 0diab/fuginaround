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


def ohmslawV(ohm,I):
    v = ohm * I
    return v
current = float(input("what is the current? "))
resistance = float(input("what is the resistance? "))

voltage =  ohmslawV(resistance,current)
print(f"The voltage is {voltage:.2f}")


def ohmslawR(v,I):
    R = v/I
    return R
voltage = float(input(f"what is the voltage? "))
current = float(input(f"what is the current? "))

resistance = ohmslawR(voltage,current)
print(f"The resistors value is {resistance:.2f}")


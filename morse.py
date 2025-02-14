A = ".-"
B = "-..."
C = "-.-."
D = "-.."
E = "."
F = "..-."
G = "--."
H = "...."
I = ".."
J = ".---"
K = "-.-"
L = ".-.."
M = "--"
N = "-."
O = "---"
P = ".--."
Q = "--.-"
R = ".-."
S = "..."
T = "-"
U = "..-"
V = ",,,-"
W = ".--"
X = "-..-"
Y = "-.--"
Z = "--.."





usr = input("what would you like to convert to Morse code: ")

for i in range(len(usr)):

    match usr[i]:
        case "A" | "a":
            print(".-", end=" ")
        case "B" | "b":
            print("-...", end=" ")
        case "C" | "c":
            print("-.-.", end=" ")
        case "D" | "d":
            print("-..", end=" ")
        case "E" | "e":
            print(".", end=" ")
        case "F" | "f":
            print("..-.", end=" ")
        case "G" | "g":
            print("--.", end=" ")
        case "H" | "h":
            print("....", end=" ")
        case "I" | "i":
            print("..", end=" ")
        case "J" | "j":
            print(".---", end=" ")
        case "K" | "k":
            print("-.-", end=" ")
        case "L" | "l":
            print(".-..", end=" ")
        case "M" | "m":
            print("--", end=" ")
        case "N" | "n":
            print("-.", end=" ")
        case "O" | "o":
            print("---", end=" ")
        case "P" | "p":
            print(".--.", end=" ")
        case "Q" | "q":
            print("--.-", end=" ")
        case "R" | "r":
            print(".-.", end=" ")
        case "S" | "s":
            print("...", end=" ")
        case "T" | "t":
            print("-", end=" ")
        case "U" | "u":
            print("..-", end=" ")
        case "V" | "v":
            print("...-", end=" ")
        case "W" | "w":
            print(".--", end=" ")
        case "X" | "x":
            print("-..-", end=" ")
        case "Y" | "y":
            print("-.--", end=" ")
        case "Z" | "z":
            print("--..", end=" ")
        case " ":
            print(f"")

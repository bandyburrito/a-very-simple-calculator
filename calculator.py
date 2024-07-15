
numri1 = float(input("Write down your the first number: "))

while True:
    sign = input("Write down the operator: ")
    if sign not in ("+", "-", "/", "*"):
        print("OPERATORI INVALID! Ju lutem perdorni njeren nga keto: +, -, /, *")
        continue
    else:
        numri2 = float(input("Write down your the second number: "))
        break

if sign == "+":
    print(numri1 + numri2)
elif sign == "-":
    print(numri1 - numri2)
elif sign == "/":
    print(numri1 / numri2)
elif sign == "*":
    print(numri1 * numri2)

while True:
    print("-------------------------------------")
    print("""SIMPLE CALC by nox
type add to add two numbers
type subtract to two numbers
type multiply to multiply two numbers
type divide to divide two numbers
type quit to quit the program
type sum to sum the number from 0 to x""")
    user = input('type: ')
    if user == "quit":
        break
    elif user == "add":
        num1 = input("Number 1: ")
        num2 = input("Number 2: ")
        ans = (int(num1) + int(num2))
        print("Your answer is: " + str(ans))
    elif user == "divide":
        num1 = input("Number 1: ")
        num2 = input("Number 2: ")
        ans = (int(num1) / int(num2))
        print("Your answer is: " + str(ans))
    elif user == "subtract":
        num1 = input("Number 1: ")
        num2 = input("Number 2: ")
        ans = (int(num1) - int(num2))
        print("Your answer is: " + str(ans))
    elif user == "multiply":
        num1 = input("Number 1: ")
        num2 = input("Number 2: ")
        ans = (int(num1) * int(num2))
        print("Your answer is: " + str(ans))
    elif user == "sum":
        num1 = input("Number: ")
        def sum(num1):
            res = 0
            for i in range(int(num1)):
                res += i
            return res
        print(sum(num1))
    else:
        print("unknown")

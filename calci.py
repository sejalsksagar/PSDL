#3372 06/09/21
#Ass0: 2. Design a calculator

print("**************** CALCULATOR *******************")
ask_again = True

while ask_again:
    try:
        num1 = float(input("Enter 1st number: "))
        op = input("Enter operator: ")
        num2 = float(input("Enter 2nd number: "))
        ask_again = False
    except:
        print("Invalid number")
        ask_again = True

    if not ask_again:
        if op == "+":
            print(num1 + num2)
        elif op == "-":
            print(num1 - num2)
        elif op == "/":
            try:
                print(num1 / num2)
            except ZeroDivisionError:
                print("Divided by zero")
        elif op == "*":
            print(num1 * num2)
        else:
            print("Invalid operator")

        ch = input("Do you want to try again? (y/n): ")
        if ch == "y":
            ask_again = True
        else:
            print("**************** PROGRAM END ******************")

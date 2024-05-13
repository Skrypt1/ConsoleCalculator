def calculations(num1, num2, op):
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    elif op == "^":
        result = num1 ** num2
    else:
        raise ValueError('Invalid Operator!')
    return int(result)

calcs = True
while calcs is True:
    num1 = int(input("Please, enter your first number: "))
    op = input('Which operation are you using? (+, -, *, /, ^) \n')
    num2 = int(input("Please, enter your second number: "))
    print(num1,op,num2)
    result = calculations(num1, num2, op)
    print("=", result)
    playMore = input("Would you like to do more calculations? (y/n): ")
    if playMore == 'n':
        calcs = False
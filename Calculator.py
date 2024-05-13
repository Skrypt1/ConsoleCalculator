nums = input("Enter the numbers, please: ")

listed = nums.split()

#print(listed)

for i in range(len(listed)):
    listed[i] = int(listed[i])

print(f"These are the integers: \n {listed}")
op = input(f"What operation do you want to do? (+, -, *, /) ")

a = int(listed[0])
b = int(listed[1])

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
else:
    result = a / b
    
print(f"The result of your equation, {a} {op} {b} is {result}.")
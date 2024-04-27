
summ = 0
num1 = int(input("Enter the first number: "))
num2 =  int(input("Enter the second number: "))

first = num1
second = num2

if num1 < num2:
    first = num2
    second = num1

for i in range(second+1,first):
    print(i)


sum=0

intpar = int(input("Enter a even and positive number: "))

while intpar%2==0:
  sum += intpar

  intpar = int(input("Enter a even and positive number: "))          


print(f"You have entered a diferent value game over\nSum of all numbers: {sum}")
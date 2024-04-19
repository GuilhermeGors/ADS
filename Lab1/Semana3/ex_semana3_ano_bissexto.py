
# ex_semana2_ano_bissexto
print("Leap yer verifier")

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
     leap = True
else:
     leap = False

if leap:
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} isn't a leap year.")



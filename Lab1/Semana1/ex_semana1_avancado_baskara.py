# ex_semana1_avancado_baskara

#   ax**2 + bx + c = 0
a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
c=int(input("Enter c value: "))

D = (b**2 - 4*a*c)
x1 = (-b + D**(1/2)) / (2*a)
x2 = (-b - D**(1/2)) / (2*a)

print(f"x' = {x1}\nx" = {x2}")


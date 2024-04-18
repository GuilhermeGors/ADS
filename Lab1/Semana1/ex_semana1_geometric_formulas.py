
# ex_semana1_geometric_formulas
#B - Base
#C - Height

print("Enter 5 integers: ")
A = int(input("1º number: "))
B = int(input("2º number: "))
C = int(input("3º number: "))
D = int(input("4º number: "))
E = float(input("5º number: "))

area_trigle        = (B*C)/2
retangle_perimeter = A+B+C+D
area_circle        = (3.14*E**2)

print(f"The triangle area is {area_trigle}")
print(f"The retangle perimeter is {retangle_perimeter}")
print(f"The circle area is {area_circle} cm²")
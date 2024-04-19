import math
# ex_semana2_calculator

def sum():
     print("\n=========\nSommator\n=========\n")
     A = float(input("Enter the value for A: "))
     B = float(input("Enter the value for b: "))
     
     print(f"{A} + {B} = {A+B}")
def sub():
     print("\n=========\nSubtractor\n=========\n")
     A = float(input("Enter the value for A: "))
     B = float(input("Enter the value for b: "))
     
     print(f"{A} - {B} = {A-B}")
     
def mult():
     print("\n=========\nMultiplicator\n=========\n")
     A = float(input("Enter the value for A: "))
     B = float(input("Enter the value for b: "))
     
     print(f"{A} * {B} = {A*B}")
     
def divide():
     print("\n=========\nDivider\n=========\n")
     A = float(input("Enter the value for A: "))
     B = float(input("Enter the value for b: "))   
     
     print(f"{A} / {B} = {A/B}")

def pot():
     print("\n=========\nPotencilizer\n=========\n")
     A = float(input("Enter the value for A: "))
     B = float(input("Enter the value for b: "))
     
     print(f"{A} ^ {B} = {A**B}")

def rad():
     print("\n=========\nRadicionalizer\n=========\n")
     A = float(input("Enter the value for A: "))
     B = float(input("Enter the value for b: ")) 
     
     print(f"{A}^(1/{B}) = {math.pow(A, 1/B)}")
     
def quit():
     print("\n=========\nBye!!\n=========\n")
     
def menu():
    print("\n=========\nCalculator\n=========\n")
    print("Enter 1 to sum 2 values")    
    print("Enter 3 to mult 2 values")
    print("Enter 4 to divide 2 values")
    print("Enter 5 to pot 2 values")
    print("Enter 6 to rad 2 values")
    print("Enter any other value to quit.")
    
    board =int(input("Option: "))
    if board==1:
        sum()
    elif board==2:
        sub()
    elif board==3:
        mult()
    elif board==4:
        divide()
    elif board==5:
        pot()
    elif board==6:
        rad()
    else: 
        quit()
        

     
    
menu()    
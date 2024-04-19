
# ex_semana3_validacao_GC
result = 0
print("\n==========\nGrade validation\n==========")
GA = float(input("Enter GA grade: "))
GB = float(input("Enter GB grade: "))

def grade_calculator():
    grade = (GA+2*GB)/3
    
    if grade<6:
       print(f"Your grade is {grade:.2f}, and you need GC exam...") 
    else:   
       print(f"Your grade is {grade:.2f} and you are aproved!") 

grade_calculator()

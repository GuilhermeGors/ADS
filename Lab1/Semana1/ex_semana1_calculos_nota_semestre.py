
# ex_semana1_calculos_nota_semestre

value_GA= 0.33
value_GB= 0.67

# GA
value_practictical_exercises =0.45 
value_teorical_exercises = 0.55

# GB
value_lab_exam = 0.6
value_extra_work = 0.2
value_teorical_test = 0.2

#=====================================================================#
print("Enter your GA grades in each option: ")

teorical_exercises = float(input("Teorical exercises: "))
practical_exercises = float(input("Practical exercises: "))

grade_GA = teorical_exercises*value_teorical_exercises + practical_exercises*value_practictical_exercises

print(f"\n**********\nYour grade on in GA was {grade_GA:.2f} \n**********\n")

print("Enter your GB grades in each option:\n ")

lab_exam = float(input("Laboratory Exam: "))
teorical_test = float(input("Teorical test: "))
extra_work  = float(input("Extra work: "))


grade_GB = lab_exam*value_lab_exam + extra_work*value_extra_work + teorical_test* value_teorical_test

print(f"\n**********\nYour grade on in GB was {grade_GB:.2f} \n**********\n")

final_grade = grade_GA+grade_GB

print(f"\n**********\nYour Final grade was {final_grade:.2f}!!\n**********\n")


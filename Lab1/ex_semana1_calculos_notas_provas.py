
# ex_semana1_calculos_notas_provas


work_result       = float(input("Enter your work result: "))
full_test_result  = float(input("Enter your Full test result: "))
basic_test        = float(input("Enter your Basic test result: "))

work_result_grade       = work_result*0.1
full_test_result_grade  = full_test_result*0.6
basic_test_grade        = basic_test*0.3

final_result = work_result_grade + full_test_result_grade + basic_test_grade
print(f"This is your result in this semester:{final_result:.2f} ")





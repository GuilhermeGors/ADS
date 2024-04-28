


person = {name, civil_state}



while True:
            
    name = input("Enter your name: ")


    print("1- single\n2- married\n3- widower'4- divorced")

    civil_state = input("Enter your civil state: ")
    if civil_state ==1:
        civil_state ='Single'
    if civil_state ==2:
        civil_state ='married'    
    if civil_state ==3:
        civil_state ='widower'
    if civil_state ==4:
        civil_state ='divorced'
    else:
        print("Invalid command")

user =''
password=''
count =1
#USER10
#PASSWOED1234
while user != 'USER10' and password != 'PASSWORD1234':
    
    user = input("Enter the user name: ")
    password = input("Enter the password : ")

    if count ==3:
      print("Maximum numers of tries reached!")
      break
      
    elif user != 'USER10' and password != 'PASSWORD1234':
       print("fail do login")
       count += 1
     
    
if  count ==3:
   print("Fail to login")
else:
   print(f"Welcome {user}!")    
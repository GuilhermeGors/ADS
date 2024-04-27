
user =''
password=''

#USER10
#PASSWOED1234
while user != 'USER10' and password != 'PASSWORD1234':
    
    user = input("Enter the user name: ")
    password = input("Enter the password : ")
    if user != 'USER10' and password != 'PASSWORD1234':
      print("fail do login")

print(f"Welcome {user}!")    
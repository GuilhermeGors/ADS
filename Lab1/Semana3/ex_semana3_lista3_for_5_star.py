


print("##---------  Shopping list  -------------##")
print("Catalog: ")

items   = []
count   = {}
catalog = ['Bread','Cheese','Ram','Nuts','Milk']


print("1- Bread\n2- Cheese\n3- Ram\n4- Nuts\n5- Milk\n6- Exit")

while True:
    choice = int(input("Wich items would you like to take: "))
    
    if choice ==1:
        items.append("Bread")
    elif choice ==2:
        items.append("Cheese")
    elif choice ==3:
        items.append("Ram")
    elif choice ==4:
        items.append("Nuts")
    elif choice ==5:
        items.append("Milk")
    elif choice==6:
        break
    else:
        print("Invalid command")   

print("Shopping Cart:")


for item in items:
    count[item] = count.get(item, 0) + 1

for i, item in enumerate(count):
    print(f"{i}- item: {count[item]} {item}")
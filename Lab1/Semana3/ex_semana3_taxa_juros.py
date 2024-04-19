
# ex_semana2_taxa_juros


price = float(input("Enter a price: "))
value =0
tax = 0

if price <= 0:
    print(f"The value {price} is invalid!")

elif price < 100:
    print("_1_")
    tax = price * 0.1
    value = price + tax

elif price <= 300:
    print("_2_")
    tax = price * 0.2
    value = price + tax

elif price <= 1000:
    print("_3_")
    tax = price * 0.5
    value = price + tax

if value != 0:
    print(f"\n==========\nValue: R${value}\nTax: R${tax}\n==========")





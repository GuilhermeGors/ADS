
# ex_semana3_preco_produto_condicao



price = float(input("Enter a price: "))

if price<0:
    print(f"Invalid price R${price}")
elif price>0 and price<30:
    print(f"low price! R${price}")
elif price>=30 and price<=50:
    print(f"High price! R${price}")
else:    
    print(f"This price is too High! R${price}")
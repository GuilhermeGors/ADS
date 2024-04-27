


count =0
vogals = ("a,e,i,o,u")

word =[]
word = input("Enter a word: ")

print(f"tamanho da palavra:{len(word)}")

for i in range(1,len(word)):
    if word[i] in vogals:
        count += 1

print(count)        
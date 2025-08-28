string = input("Digite um texto: ")

for i in range(len(string)):
    if string[-i] == " ":
        index = i-1
        break

string = string[-index:]

print(string)
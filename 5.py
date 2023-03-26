string_original = input("Digite uma palavra: ") # string a ser invertida
string_invertida = ""  # string para armazenar o resultado da inversão

# função para inverter a string
for i in range(len(string_original)-1, -1, -1):
    string_invertida += string_original[i]

print(string_invertida)
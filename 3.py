
soma = 0
numA = 1
numB = 2
numC = 2 

# A
for i in range(4):
    numA += 2
print(numA)
# B
for i in range(6):
    print(numB)
    numB *= 2
print(numB)

# C
naturais = range(1, 10)
quadrados = [n**2 for n in naturais]
indice_49 = quadrados.index(49)
proximo_quadrado = quadrados[indice_49 + 1]
print(proximo_quadrado) # saída: 64

# D
while numC**2 <= 100:
    print(numC**2)
    numC += 2
# E
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
# F
def sequencia():
    
    seq = [2, 10, 12, 16, 17, 18]

    seq.append(seq[-6] + 2)
    seq.append(seq[-5] + 2)
    seq.append(seq[-4] + 4)
    seq.append(seq[-3] + 1)
    seq.append(seq[-2] + 1)
    seq.append(seq[-1] + 1)
    return seq

print(sequencia())


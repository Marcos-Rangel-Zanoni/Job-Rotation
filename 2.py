num = int(input("Digite um número: "))

fibonacci = [0, 1]  # Inicia a sequência com 0 e 1

while fibonacci[-1] < num:  # Enquanto o último valor for menor que o número informado
    fibonacci.append(fibonacci[-1] + fibonacci[-2])  # Adiciona o próximo valor na sequência

if num in fibonacci:
    print(f"O número {num} pertence à sequência de Fibonacci!")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci!")
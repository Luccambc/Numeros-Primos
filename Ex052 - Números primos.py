num = int(input("Digite um número inteiro: "))

contador = 1
for c in range(1, num):
    if num % c == 0:
        contador += 1
if contador > 2:
    print(f"Número de divisores: {contador}")
    print(f"O número {num} não é primo!")
elif contador == 2:
    print(f"Número de divisores: {contador}")
    print(f"O número {num} é primo!")
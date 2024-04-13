#2. Fazer um programa para encontrar todos os números pares entre 1 e 100

print("Programa que encontra todos números primos entre 1 e 100.")
print(100*"-")
lista = []
numero =0
num_freq = 0
for numero in range(1,101):
    if numero%2 !=0:
        print(f"{numero} é ímpar")
    else:
        print(f"{numero} é par")
        num_freq+=1
        lista.append(numero)
print(f"Foram encontrados {num_freq} números pares")
print(f"Números primos de 1 a 100: {lista}")
print(100*"-")
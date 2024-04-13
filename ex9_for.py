#9. Faça um algoritmo que leia 10 números inteiros, armazene-os em uma lista e imprima em ordem crescente.

print("Programa que lê 10 números para imprimi-los em ordem crescente!")
print(100*"-")
lista = []
for i in range(1,11):
    numeros = int(input("Digite um número inteiro: "))
    lista.append(numeros)
lista.sort()
print(lista)
print(100*"-")

#8. Faça um algoritmo que leia um número positivo e imprima seus divisores

print("Programa que calcula quais são os divisores de um número")
print(100*"-")
lista = []
while True:
    numero = int(input("Digite um número postivo: "))
    if numero<0:
       print("Número inválido, tente novamente!")
       continue
    else:
        break
for i in range(1,numero+1):
    div = numero%i
    if div ==0:
        lista.append(i)
print(f"Esses são os divisores do número {numero}: {lista}")
print(100*"-")
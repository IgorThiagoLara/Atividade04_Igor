#7. Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.

print("Programa que calcula quais são os 50 primeiros números pares e faz a soma de todos eles!")
print(100*"-")
somaPares = 0
pares = []
for i in range(1,101):
    if i%2==0:
        pares.append(i)
        somaPares = somaPares+i
print(f"O número de {len(pares)} pares foi atingido")
print(f"Esses são todos os 50 primeiros números pares: {pares}")
print(f"A soma de todos eles são: {somaPares}")
print(100*"-")

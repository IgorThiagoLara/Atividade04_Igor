#10. Dada a lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6] imprima o número que se repete mais vezes.

print("Programa que detecta qual o número mais repetido de uma lista.")
print(100*"-")
lista = [2,4,7,2,3,1,0,2,6]
num_freq = 0
num_repet = 0
for num in lista:
    if lista.count(num)>num_freq:
        num_freq +=1
        num_repet =num
print(f"O número que mais se repete é o {num_repet} e ele aparece {num_freq} vezes.")
print(100*"-")
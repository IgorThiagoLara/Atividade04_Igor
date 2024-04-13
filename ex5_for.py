#5. Ler 10 números e imprimir quantos são pares e quantos são ímpares

listaPar = []
listaImpar = []
print("Programa que lê 10 números e informa quais e quantos deles são pares ou ímpares.")
print(100*"-")
for i in range(1,11):
    numeros = int(input(f"Digite o {i}° número: "))
    par=numeros%2==0
    if par:
        listaPar.append(numeros)
    else:
        listaImpar.append(numeros)
listaPar.sort(), listaImpar.sort()
print(f"o número de pares é: {len(listaPar)} e o número de ímpares é: {len(listaImpar)}")
print(f"Pares = {listaPar} e ímpares = {listaImpar}")
print(100*"-")
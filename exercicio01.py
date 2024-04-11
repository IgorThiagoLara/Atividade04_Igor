#Exercício01
'''for numero in  range(1,51):
    print(numero)
#Exercício 02
numero =0
for numero in range(0,101):
    if numero%2 !=0:
        print(f"{numero} é ímpar")
    else:
        print(f"{numero} é par")'''

'''i = 0
for i in range(1, 101):
    if i % 2 == 0:
        par = i
    else:
        impar = i
print(f"Números impares: {impar} e números pares: {par}")'''

#Exercício 03 
'''contador=0
cont=0
print("Tabuada de 1 a 10")
print(100*"-")
while contador<1:
    numeros = int(input("Digite um valor de 1 a 10: "))
    if numeros >10 or numeros <=0:
        print("Número inválido, tente novamente!!")
        continue
    contador+=1
    for i in range(1,11):
        if numeros <=10:
            tabuada=numeros*i
            print(f"{cont+1}° tabuada = {tabuada} ")
    if numeros >10 or numeros <=0:
        print("Número inválido, tente novamente!")
print(100*"-")'''

#4. Leia várias idades e calcule a média entre as idades (usar uma variável para idade)
'''print("Programa para calcular a média de idades de um grupo de 10 pessoas.")
somaIdades = 0
lista = list()
for i in range(1,11):
    idade = int(input("Digite uma idade: "))
    if idade <0:
        print("Número inválido. tente novamente!")
        continue
    lista.append(idade)
    somaIdades= somaIdades+idade
media = somaIdades/len(lista)
print(f"A média do grupo de pessoas é {media:.2f}")'''

#5. Ler 10 números e imprimir quantos são pares e quantos são ímpares
'''listaPar = []
listaImpar = []
print("Programa para verificar se os 10 números digitados são pares ou ímpares")
for i in range(1,11):
    numeros = int(input("Digite um número: "))
    if numeros<0:
        print("Número inválido, tente novamente!")
        continue
    par=numeros%2==0
    if par:
        print("O número é par")
        listaPar.append(numeros)
    else:
        print("O número é ímpar")
        listaImpar.append(numeros)
print(f"o número de pares é: {len(listaPar)}")
print(f"o número de ímpares é: {len(listaImpar)}")'''



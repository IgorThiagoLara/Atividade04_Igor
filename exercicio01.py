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

'''6. Utilizando a estrutura de repetição for, faça um programa que receba 10
números e conte quantos deles estão no intervalo [10,20] e quantos
deles estão fora do intervalo.'''
'''print("Programa que contabiliza quantos números digitados estão entre o intervalo de 10 e 20.")
print(100*"-")
numerosInterv = []
for i in range(1,11):
    numeros = int(input("Digite um número: "))
    if numeros <0:
        print("Número considerado inválido para o teste, tente novamente!")
        continue
    if numeros >=10 and numeros<=20:
        numerosInterv.append(numeros)
print(f"Você digitou {len(numerosInterv)} números entre 10 e 20")
print(100*"-")'''

#7. Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.
'''somaPares = 0
pares = []
for i in range(1,101):
    if i%2==0:
        print(f"O número {i} é par")
        pares.append(i)
        somaPares= somaPares+i
print(len(pares))
print(f"A soma de todos os 50 primeiros números pares é: {somaPares}")'''

#8. Faça um algoritmo que leia um número positivo e imprima seus divisores
'''lista = []
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
print(f"Esses são os divisores do número {numero}: {lista}")'''

#6. Utilizando a estrutura de repetição for, faça um programa que receba 10 números e conte quantos deles estão no intervalo [10,20] e quantos deles estão fora do intervalo.
print("Programa que contabiliza quantos números digitados estão entre o intervalo de 10 e 20.")
print(100*"-")
numerosInterv = []
numerosOut = []
for i in range(1,11):
    numeros = int(input(f"Digite o {i}° número: "))
    if numeros <0:
        print("Número considerado inválido para o teste, tente novamente!")
        continue
    if numeros >=10 and numeros<=20:
        numerosInterv.append(numeros)
    else:
        numerosOut.append(numeros)
print(f"Você digitou {len(numerosInterv)} números entre o intervalo 10 e 20 e {len(numerosOut)} números fora dele.")
print(100*"-")
#3. Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever a tabuada de 1 a 10 do valor lido.

print("Tabuada de 1 a 10.")
print("Digite 0 quando quiser que o programa encerre!")
print(100*"-")
while True:
    numero = int(input("Digite um valor de 1 a 10: "))
    if numero ==0:
        print("Programa finalizando....")
        break
    if numero >10 or numero <0:
        print("Número inválido, tente novamente!!")
        continue
    for i in range(1,11):
        if numero <=10:
            tabuada=numero*i
            print(f"{i} X {numero} = {tabuada} ")
print(100*"-")
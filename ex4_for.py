#4. Leia várias idades e calcule a média entre as idades (usar uma variável para idade)

print("Programa para calcular a média de idades de um grupo.")
print(100*"-")
tamanho = int(input("Digite quantas pessoas pessoas há no grupo para calcular: "))
somaIdades = 0
lista = []
for i in range(1,tamanho+1):
    idade = int(input("Digite uma idade: "))
    if idade <0:
        print("Número inválido. tente novamente!")
        continue
    lista.append(idade)
    somaIdades= somaIdades+idade
media = somaIdades/len(lista)
print(f"A média do grupo de pessoas é {media:.2f}.")
print(100*"-")

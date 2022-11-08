import time
from Queue import Queue


batataQuente = Queue()

pessoas = int(input("Digite a quantidade de pessoas que irá participar: "))

for x in range(pessoas):
    jogadores = str(input("Escreva o nome do jogador nº {contador}: ".format(contador = x+1)));
    # batataQuente.push(jogadores)

while True:
    numero_de_queimado = int (input("Digite a quantidade de quentes que sera dito: "))

    for x in range (numero_de_queimado) :
        # WARN ❗ Posição na memória onde guardamos a Queue();
        # NOTE ❗ print(batataQuente)
        print("Jogada nº {contador} 🔥".format(contador = x + 1))
        time.sleep(1)
        # batataQuente.push(batataQuente.first.data)
        # batataQuente.pop()
    print("🏐 Queimado!")

    print("{jogadorQueimado} FOI QUEIMADO!".format(jogadorQueimado = batataQuente.first.data))
    # batataQuente.pop()

    if batataQuente._size == 1:
        print("{jogadorVencedor} ganhou o jogo!".format(jogadorVencedor = batataQuente.first.data))
from Queue import Queue

fila = Queue();
filaNormal = Queue();
filaPrioritaria =  Queue();

limitePessoas = int(input("Quantas pessoas serão cadastradas? "));

contadorNormal = 0;
contadorPrioritaria = 0;

for pessoa in range(limitePessoas):
    print("Qual sua idade?")
    print("Digite [1] caso possua de 20 à 49 anos.")
    print("Digite [2] caso possua 59 anos ou mais.")
    print("Digite [0] para sair.")
    inputIdade = int(input())

    if inputIdade == 0:
        break;

    if inputIdade == 1:
        senha = "N{senha}".format(senha = contadorNormal + 1);

        fila.push(senha);
        filaNormal.push(senha);
        continue;

    elif inputIdade == 2:
        senha = "P{senha}".format(senha = contadorPrioritaria + 1);

        fila.push(senha);
        filaPrioritaria.push(senha);
        continue;

    else:
        print("INPUT inválida")

# TODO :: Forma para exibir a variávela fila e o código estaria encerrado.
while fila._len_() != 0:
    proximo = fila.first.next;

    if fila.first.data.startswith('P'):
        print("Sim, sou prioritário");

    if proximo.data.startswith('P'):
        print("Sim, o próximo é uma senha prioritária")
        fila.pop();

        if proximo.data.startswith('P'):
            print("Sim, o próximo do próximo é uma senha prioritária")

    fila.pop();



# print("-="*20);
# print(" ORDEM DAS FILAS: ");
# print("-="*20);
# while prioritario._size != 0 or normal._size != 0:
#     cont = 0
#     for n in range(3):
#         if prioritario._size != 0:
#             print(" ATENDIMENTO PRIORITARIO");
#             print("P ", prioritario.pop());

#     if normal._size != 0:
#         print (" ATENDIMENTO NORMAL");
#         print ("N ", normal.pop());
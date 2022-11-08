from Node import Node 
class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elem):
        #insere um elemento na pilha
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size = self._size + 1

    def pop(self):
        # remove o elemento do topo da pilha
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node.data
        raise IndexError("The stack is empty")

    def peek(self):
        # retorna o topo sem remover
        if self._size > 0:
            return self.top.data
        raise IndexError("The stack is empty")

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def __repr__(self):
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()

codigos = Stack()
container1 = Stack()
container2 = Stack()
container3 = Stack()
container4 = Stack()
menor = 0

while True:
    print(container1)
    print(container2)
    print(container3)
    print(container4)
    opcao = input('''Digite a opção desejada:
[1] - Adicionar container
[2] - Remover container
''')

    if opcao == "1":
        codValido = True
        while True:
            container = input("Informe o código do container, ou digite [0] para retornar: ")
            if container == "0":  break
            codigos.push(container)
            
            #Verificar validade do código digitado
            if codigos.top.next != None:
                aux = codigos.top.next
                while True:
                    if aux.data == container:
                        codValido = False
                        break
                    if aux.next != None:
                        aux = aux.next
                    else: break
            
            if codValido == False:
                print("🚫 \nCódigo inválido!\n 🚫")
                break
            else:
                #Verificar menor pilha
                if len(container1) > menor and len(container2) > menor and len(container3) > menor and len(container4) > menor:
                    menor = len(container1)
                if len(container1) < menor:
                    menor = len(container1)
                elif len(container2) < menor:
                    menor = len(container2)
                elif len(container3) < menor:
                    menor = len(container3)
                elif len(container4) < menor:
                    menor = len(container4)     

                #Adicionar container à pilha
                if len(container1) == menor and len(container1) < 3:
                    container1.push(container)
                elif len(container2) == menor and len(container2) < 3:
                    container2.push(container)
                elif len(container3) == menor and len(container3) < 3:
                    container3.push(container)
                elif len(container4) == menor and len(container4) < 3:
                    container4.push(container)
                    menor = len(container4)
                else:
                    print("🚫 \nImpossível empilhar!\n 🚫")
                    break
                print("✅ Container adicionado com sucesso! ✅")


    elif opcao == "2":
        while True:
            remover = input("Informe o código do container para remover, ou [0] para retornar: ")
            codRemValido = False
            removeu = False
            if remover == "r": break

            #Verificar validade do código digitado
            if codigos.top != None:
                aux = codigos.top
                while True:
                    if aux.data == remover:
                        codRemValido = True
                        break
                    if aux.next != None:
                        aux = aux.next
                    else: break


            #Remover container da pilha
            if len(container1) == 0 and len(container2) == 0 and len(container3) == 0 and len(container4) == 0:
                print("Impossível desempilhar! 🚫")
                break
            if codRemValido == False:
                print("🚫 Código inválido! 🚫")
            else:
                if len(container1) != 0: 
                    if container1.top.data == remover:
                        container1.pop()  
                        menor = len(container1)
                        removeu = True
                if len(container2) != 0:   
                    if container2.top.data == remover:
                        container2.pop()
                        menor = len(container2)
                        removeu = True
                if len(container3) != 0:
                    if container3.top.data == remover:
                        container3.pop()
                        menor = len(container3)
                        removeu = True
                if len(container4) != 0:
                    if container4.top.data == remover:
                        container4.pop()
                        menor = len(container4)
                        removeu = True
                if removeu == False:
                    print("Impossível desempilhar! 🚫")
                    break

                #Repreencher a lista de códigos sem o código do container removido
                if removeu == True:
                    remCodigos = (len(codigos) - 1)
                    n = codigos.top
                    while codigos.top != None:
                        codigos.pop()
                    while len(codigos) < remCodigos:
                        if n.data != remover:
                            codigos.push(n.data)
                        if n.next != None:
                            n = n.next

                print("✅ Container desempilhado com sucesso. ✅")
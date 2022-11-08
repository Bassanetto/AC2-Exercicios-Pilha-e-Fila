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

while True:
    input = input("Digite a expressão matemática desejada: ")
    abreExpressao = Stack()
    fechaExpressao = Stack()
    valido = True
  
    for x in input:
        if x == "(":
            abreExpressao.push(x)
        elif x == ")": 
            fechaExpressao.push(x)
            #Verificar a condição 2.
            if len(fechaExpressao) > len(abreExpressao):
                valido = False

    #Verificar a condição 1.
    if len(abreExpressao) != len(fechaExpressao):
        valido = False

    if valido == True:
        print("=======================")
        print("✅ Expressão válida. ✅")
        print("=======================")
    else:
        print("=======================")
        print("🚫 Expressão inválida. 🚫")
        print("=======================")

from Node import Node 

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elem):
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size = self._size + 1

    def pop(self):
        if self._size >0:
            elem = self.top.data
            self.top = self.top.next
            self._size -=1
            return elem
        raise IndexError("The stack is empty")

    def peek(self):
        if self._size > 0:
            return self.top.data
        raise IndexError("The stack is empty")


    def _len_(self):
        """Retorna o tamanho da lista"""
        return self._size

    def _repr_(self):
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next  
        return r

    def _str_(self):
        return self._repr_()

pilhaAberta = Stack()

expressao = str(input("Digite uma Expressão Aritmética: "))

for simbolo in expressao:
    if simbolo == "(":
        pilhaAberta.push("(")   
    elif simbolo == ")":
        if len(pilhaAberta) >0:
            pilhaAberta.pop()
        else:
            pilhaAberta.push(")")
            break
if len (pilhaAberta) ==0:
    print ("Sua expressão Aritimética está certa!")
else:
    print ("Sua expressão Aritimética está errada!")
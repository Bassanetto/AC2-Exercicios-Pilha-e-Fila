class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def push(self, elem):
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node  
        if self.first is None:
            self.first = node
        self._size = self._size + 1

    def pop(self):
        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next
            if self.first is None:
                self.last = None
            self._size = self._size - 1
            return elem
        raise IndexError("A fila está vazia")

    def peek(self):
        if self._size > 0:
            elem = self.first.data
            return elem
        raise IndexError("A fila está vazia")

    def _len_(self):
        """Retorna o tamanho da lista"""
        return self._size

    def _repr_(self):
        r = ""
        pointer = self.first
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r

    def _str_(self):
        return self._repr_()
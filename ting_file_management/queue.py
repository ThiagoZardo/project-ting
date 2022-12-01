class Queue:
    def __init__(self):
        self.values = []
        self.__length = 0

    def __len__(self):
        return self.__length

    def enqueue(self, value):
        self.__length += 1
        return self.values.append(value)

    def dequeue(self):
        self.__length -= 1
        return self.values.pop(0)

    def search(self, index):
        if index < 0 or not isinstance(index, int) or index > self.__length:
            raise IndexError
        
        lista = self.values
        return lista[index]

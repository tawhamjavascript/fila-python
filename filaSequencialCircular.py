

class Fila:
    def __init__(self, length: int):
        self.__lengthMax = length
        self.__data = [None] * self.__lengthMax
        self.__head = 0
        self.__end = -1
        self.__elementsInQueue = 0

    def is_empty(self) -> bool:
        return self.__elementsInQueue == 0

    def is_full(self):
        return self.__elementsInQueue == self.__lengthMax

    def __len__(self):
        return self.__elementsInQueue

    def head_of_queue(self):
        return self.__data[self.__head]

    def find(self, value):
        head = self.__head
        for i in range(1, self.__lengthMax + 1):
            if self.__data[head] == value:
                return i

            head = (head + 1) % self.__lengthMax

    def to_queue(self, value):
        self.__elementsInQueue += 1
        self.__end = (self.__end + 1) % self.__lengthMax
        self.__data[self.__end] = value

    def dequeue(self):
        head = self.head_of_queue()
        self.__elementsInQueue -= 1
        self.__head = (self.__head + 1) % self.__lengthMax
        return head


fila = Fila(3)
fila.to_queue(20)
fila.to_queue(30)
print(fila.dequeue())





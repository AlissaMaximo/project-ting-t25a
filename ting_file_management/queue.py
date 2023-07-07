from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._data = list()
        self._length = 0

    def __len__(self):
        """Aqui irá sua implementação"""
        return self._length

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self._data.append(value)
        self._length += 1

    def dequeue(self):
        """Aqui irá sua implementação"""
        if len(self._data) == 0:
            return None
        self._length -= 1
        return self._data.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if len(self._data) == 0 or index >= len(self._data) or index < 0:
            raise IndexError("Índice Inválido ou Inexistente")

        return self._data[index]

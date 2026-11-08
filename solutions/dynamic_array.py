class DynamicArray:
    def __init__(self):
        self._size = 0
        self._capacity = 4
        self._data = [None] * self._capacity

    @property
    def capacity(self):
        return self._capacity

    def __len__(self):
        return self._size

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def append(self, item):
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._size] = item
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise IndexError("pop from empty array")
        last_item = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return last_item

    def __getitem__(self, index):
        if not isinstance(index, int) or index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        return self._data[index]

    def __setitem__(self, index, value):
        if not isinstance(index, int) or index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        self._data[index] = value

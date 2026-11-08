class Deque:
    def __init__(self):
        self._capacity = 4
        self._buffer = [None] * self._capacity
        self._head = 0
        self._tail = 0
        self._size = 0

    @property
    def capacity(self):
        return self._capacity

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _resize(self):
        new_capacity = self._capacity * 2
        new_buffer = [None] * new_capacity
        
        for i in range(self._size):
            new_buffer[i] = self._buffer[(self._head + i) % self._capacity]
        
        self._buffer = new_buffer
        self._capacity = new_capacity
        self._head = 0
        self._tail = self._size

    def push_back(self, item):
        if self._size == self._capacity:
            self._resize()
        
        self._buffer[self._tail] = item
        self._tail = (self._tail + 1) % self._capacity
        self._size += 1

    def push_front(self, item):
        if self._size == self._capacity:
            self._resize()
        
        self._head = (self._head - 1) % self._capacity
        self._buffer[self._head] = item
        self._size += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError
        
        item = self._buffer[self._head]
        self._buffer[self._head] = None
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        return item

    def pop_back(self):
        if self.is_empty():
            raise IndexError
        
        self._tail = (self._tail - 1) % self._capacity
        item = self._buffer[self._tail]
        self._buffer[self._tail] = None
        self._size -= 1
        return item

    def front(self):
        if self.is_empty():
            raise IndexError
        return self._buffer[self._head]

    def back(self):
        if self.is_empty():
            raise IndexError
        return self._buffer[(self._tail - 1) % self._capacity]

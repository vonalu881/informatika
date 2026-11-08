class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data, next=None, prev=self.tail)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data, next=self.head, prev=None)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        current = self.head
        
        while current is not None:
            if current.data == data:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
                if self.head is not None:
                    self.head.prev = None
                if self.tail is not None:
                    self.tail.next = None
                return
            current = current.next

    def to_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def to_list_reverse(self):
        result = []
        current = self.tail
        while current is not None:
            result.append(current.data)
            current = current.prev
        return result

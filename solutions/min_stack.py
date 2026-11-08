class MinStack:
    def __init__(self):
        self.items = []
        self.min_items = []

    def __len__(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)
        
        if len(self.min_items) == 0:
            self.min_items.append(item)
        else:
            current_min = self.min_items[-1]
            if item < current_min:
                self.min_items.append(item)
            else:
                self.min_items.append(current_min)

    def pop(self):
        if len(self.items) == 0:
            raise IndexError
            
        self.min_items.pop()
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            raise IndexError
        return self.items[-1]

    def get_min(self):
        if len(self.items) == 0:
            raise IndexError
        return self.min_items[-1]

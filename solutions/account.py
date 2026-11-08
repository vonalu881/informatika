class Account:
    def __init__(self, number, owner, balance=0):
        if balance < 0:
            raise ValueError
        self.number = number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        self.balance = self.balance - amount

    def __repr__(self):
        return f"Account('{self.number}', '{self.owner}', {self.balance})"

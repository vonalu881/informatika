class Account:
    def __init__(self, number, owner, balance=0):
        if balance < 0:
            raise ValueError
        self.number = number
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError
        if amount > self.balance:
            raise ValueError
        self._balance -= amount

    def __repr__(self):
        return f"Account('{self.number}', '{self.owner}', {self.balance})"

class SavingsAccount(Account):
    def __init__(self, number, owner, balance=0, rate=0.05):
        super().__init__(number, owner, balance)
        self.rate = rate

    def add_interest(self):
        self._balance += self._balance * self.rate

    def __repr__(self):
        return f"SavingsAccount('{self.number}', '{self.owner}', {self._balance}, {self.rate})"

class CheckingAccount(Account):
    def __init__(self, number, owner, balance=0, overdraft=0):
        super().__init__(number, owner, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError
        if self._balance + self.overdraft < amount:
            raise ValueError
        self._balance -= amount

    def __repr__(self):
        return f"CheckingAccount('{self.number}', '{self.owner}', {self._balance}, {self.overdraft})"

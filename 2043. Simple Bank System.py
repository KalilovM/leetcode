from typing import List


class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (0 <= account1 - 1 <= len(self.balance)) and (
            0 <= account2 - 1 <= len(self.balance)
        ):
            if self.balance[account1 - 1] - money < 0:
                return False
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if 0 <= account - 1 <= len(self.balance):
            self.balance[account - 1] += money
            return True
        else:
            return False

    def withdraw(self, account: int, money: int) -> bool:
        if 0 <= account - 1 <= len(self.balance):
            if self.balance[account - 1] - money >= 0:
                self.balance[account - 1] -= money
                return True
        return False


obj = Bank([10, 100, 20, 50, 30])
withdraw = obj.withdraw(3, 10)
print(withdraw)

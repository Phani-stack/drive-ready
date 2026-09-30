from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(slef, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


class UPI(Payment):
    def pay(slef, amount):
        print("Paid", amount)

    def refund(self, amount):
        print("Refunded", amount)

def checkout(method, amount):
    method.pay(amount)

def main():
    checkout(UPI(), 300)

main()

"""Employee pay calculator."""

from abc import (
    ABC,
    abstractmethod,
)

class Employee:
    def __init__(self, name, contract, commission=None):
        self.name = name
        self.contract = contract
        if commission:
            self.commission = commission
        else:
            self.commission = NoCommission()

    def get_pay(self):
        return self.contract.get_pay() + self.commission.get_commission()

    def __str__(self):
        return f"{self.name}{self.contract}{self.commission}.  Their total pay is {self.get_pay()}."

#contracts
class Contract(ABC):
    @abstractmethod
    def get_pay(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class MonthlyContract(Contract):
    def __init__(self, salary):
        self.salary = salary

    def get_pay(self):
        return self.salary

    def __str__(self):
        return f" works on a monthly salary of {self.salary}"

class HourlyContract(Contract):
    def __init__(self, hours, wage):
        self.hours = hours;
        self.wage = wage;

    def get_pay(self):
        return self.hours*self.wage

    def __str__(self):
        return f" works on a contract of {self.hours} hours at {self.wage}/hour"

#commissions
class Commission(ABC):
    @abstractmethod
    def get_commission(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class NoCommission(Commission):
    def get_commission(self):
        return 0

    def __str__(self):
        return ""

class ContractCommission(Commission):
    def __init__(self, contracts, rate):
        self.contracts = contracts
        self.rate = rate

    def get_commission(self):
        return self.contracts*self.rate

    def __str__(self):
        return f" and receives a commission for {self.contracts} contract(s) at {self.rate}/contract"

class BonusCommission(Commission):
    def __init__(self, bonus):
        self.bonus = bonus

    def get_commission(self):
        return self.bonus

    def __str__(self):
        return f" and receives a bonus commission of {self.bonus}"

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', MonthlyContract(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlyContract(100,25))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', MonthlyContract(3000), ContractCommission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlyContract(150,25), ContractCommission(3,220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', MonthlyContract(2000), BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlyContract(120,30), BonusCommission(600))

class Account:
    def __init__(self,ac_no,ac_holder, balance):
        self._ac_no = ac_no
        self._ac_holder = ac_holder
        self._balance = balance

    def set_ac(self, ac_no):
        self._ac_no = ac_no

    def get_ac(self):
        return self._ac_no

    def set_holder(self, holder):
        self._ac_holder = holder

    def get_holder(self):
        return self._ac_holder

    def set_balance(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance += amount

    def display_info(self):
        print('Account No: ',self._ac_no, '\nHolder name: ', self._ac_holder, '\nBalance: ', self._balance)
        print('\n\n')

class SavingsAccount(Account):
    def __init__(self,ac_no,ac_holder, balance, interest_rate):
        self.interest_rate = interest_rate
        self._ac_no = ac_no
        self._ac_holder = ac_holder
        self._balance = balance

    def display_info(self):
        print('Account No: ',self._ac_no, '\nHolder name: ', self._ac_holder, '\nBalance: ', self._balance, '\nInterest: ', self.interest_rate)
        print('\n\n')


class CheckingAccount:
    def __init__(self, ac_no,ac_holder, balance, interest_rate, overdraft_limit ):
        self.interest_rate = interest_rate
        self._ac_no = ac_no
        self._ac_holder = ac_holder
        self._balance = balance
        self._overdraft_limit = overdraft_limit

    def withdraw(self):
        print('Hangle overdraft')
        #handle overdraft

    def display_info(self):
        print('Dis')


user1 = Account(4, 'Rasel', 500)
user1.display_info()

user2 = SavingsAccount(5, 'Sajib', 1000, 15)
user2.display_info()


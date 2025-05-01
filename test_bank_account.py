import unittest
from bank_account import bank_account
# This is a simple bank account management system
# that allows users to create, view, and delete accounts.
# It uses a class to represent a bank account and includes
# methods for depositing and withdrawing money.

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self):
        return self.balance
class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("John Doe", 1000)

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)

    def test_withdraw(self):
        self.account.withdraw(300)
        self.assertEqual(self.account.get_balance(), 700)

    def test_overdraw(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(2000)
    def test_negative_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

import unittest
from bank_account import BankAccount
class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("John Doe", 1000)

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)

    def test_withdraw(self):
        self.account.withdraw(300)
        self.assertEqual(self.account.get_balance(), 700)

    def test_overdraw(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(2000)

            
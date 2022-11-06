'''Exercise 1: Bank Account
Instructions
Part I:

Create a class called BankAccount that contains the following attributes and methods:
balance - (an attribute)
__init__ : initialize the attribute
deposit : - (a method) accepts a positive int and adds to the balance, raise an Exception if the int is not positive.
withdraw : - (a method) accepts a positive int and deducts from the balance, raise an Exception if not positive


Part II : Minimum balance account

Create a MinimumBalanceAccount that inherits from BankAccount.
Extend the __init__ method and accept a parameter called minimum_balance with a default value of 0.
Override the withdraw method so it only allows the user to withdraw money if the balance remains higher than the minimum_balance, raise an Exception if not.


Part III: Expand the bank account class

Add the following attributes to the BankAccount class:
username
password
authenticated (False by default)

Create a method called authenticate. This method should accept 2 strings : a username and a password. If the username and password match the attributes username and password the method should set the authenticated boolean to True.

Edit withdraw and deposit to only work if authenticated is set to True, if someone tries an action without being authenticated raise an Exception


Part IV: BONUS Create an ATM class

__init__:
Accepts the following parameters: account_list and try_limit.

Validates that account_list contains a list of BankAccount or MinimumBalanceAccount instances.
Hint: isinstance()

Validates that try_limit is a positive number, if you get an invalid input raise an Exception, then move along and set try_limit to 2.
Hint: Check out this tutorial

Sets attribute current_tries = 0

Call the method show_main_menu (see below)

Methods:
show_main_menu:
This method will start a while loop to display a menu letting a user select:
Log in : Will ask for the users username and password and call the log_in method with the username and password (see below).
Exit.

log_in:
Accepts a username and a password.

Checks the username and the password against all accounts in account_list.
If there is a match (ie. use the authenticate method), call the method show_account_menu.
If there is no match with any existing accounts, increment the current tries by 1. Continue asking the user for a username and a password, until the limit is reached (ie. try_limit attribute). Once reached display a message saying they reached max tries and shutdown the program.

show_account_menu:
Accepts an instance of BankAccount or MinimumBalanceAccount.
The method will start a loop giving the user the option to deposit, withdraw or exit.'''

class BankAccount:

    def __init__(self, balance, username, password):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = False

    def authenticate(self, user, pw):
        if user == self.username and pw == self.password:
            self.authenticated = True
            print("User connected and authenticated. Welcome to your bank account.")
        else:
            print("Invalid Credentials.")
        return self.authenticated


    def deposit(self, amount):
        if self.authenticated:
            if amount <= 0:
                raise Exception("Invalid amount.")
            else:
                self.balance += amount
                print(f"You have deposited ${amount} into your account. Your current balance is ${self.balance}.")
                return self.balance
        else:
            raise Exception("User is not connected to the account.")

    def withdraw(self, amount_drawn):
        if self.authenticated:
            if amount_drawn <= 0:
                raise Exception("Can't withdraw this amount. Invalid value.")
            elif amount_drawn > self.balance:
                print(f"Your withdraw request of ${amount_drawn} cannot be completed due to lack of funds. Your current balance is ${self.balance}.")
            else:
                self.balance -= amount_drawn
                print(f"You have withdrawn ${amount_drawn} from your account. Your current balance is ${self.balance}.")
                return self.balance
        else:
            raise Exception("User is not connected to the account..")
#
# mybank = BankAccount(1000,'ron','123ron')
# print(mybank.deposit(500))
# # print(mybank.withdraw(-500))
# print(mybank.withdraw(1400))

class MinimumBalanceAccount(BankAccount):

    def __init__(self, minimum_balance, username, password):
        super().__init__(minimum_balance, username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount_drawn):
        if self.balance > self.minimum_balance and amount_drawn < self.balance:
            self.balance -= amount_drawn
            print(f"You withdrew ${amount_drawn} from your bank account. Your current balance is ${self.balance}.")
        else:
            raise Exception(f"You do not have enough funds to complete this operation. Current balance: ${self.balance}.")

newbank = MinimumBalanceAccount(500,'ronn','123ronn')

class ATM:

    def __init__(self, account_list, try_limit):
        self.account_list = []
        for accounts in account_list:
            if isinstance(accounts, BankAccount) == True or isinstance(accounts, MinimumBalanceAccount) == True:
                self.account_list = account_list
            else:
                print(f"The account {accounts} is not available. ")
        try:
            assert try_limit > 0
        except:
            raise AssertionError("Not a valid number")
            self.try_limit = 2
        else:
            self.try_limit = try_limit

        self.current_tries = 0

    def show_main_menu(self):
        user_req = True
        while user_req:
            print('''
            LOG IN - 1
            EXIT - 2''')
            user_req = int(input("Please choose an action: "))
            if user_req == 1:
                return self.log_in()
            elif user_req == 2:
                print("Disconnected.")
                break
            else:
                print("Not a valid option. Please choose one of the options provided above.")
                return self.show_main_menu()

    def log_in(self):
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        username_list = [account.username for account in self.account_list]
        for account in self.account_list:
            if account.username == username:
                if account.password == password:
                    account.authenticate(username, password)
                    return self.show_account_menu(account)
                else:
                    self.current_tries += 1
                    while self.current_tries < self.try_limit:
                        return self.log_in()
                    else:
                        print("You have reached the maximum attempts to connect.")
                        return
            if username not in username_list:
                self.current_tries += 1
                while self.current_tries < self.try_limit:
                    return self.log_in()
                else:
                    print("You have reached the maximum attempts to connect.")
                    return

    def show_account_menu(self, account):
        if isinstance(account, BankAccount) == True or isinstance(account, MinimumBalanceAccount) == True:
            self.account = account
        self.authenticated = True
        user_input = True
        while user_input:
            print('''
            1 - DEPOSIT
            2 - WITHDRAW
            3 - CHECK BALANCE
            4 - EXIT''')
            user_input = int(input("Please choose one of the options according to its NUMBER: "))
            if user_input == 1:
                deposit_amount = int(input("Please enter the amount to be deposited into the account: $"))
                account.deposit(deposit_amount)
                return self.extra_operation()
            elif user_input == 2:
                withdraw_amount = int(input("Please enter the amount to be withdrawn from the account: $"))
                account.withdraw(withdraw_amount)
                return self.extra_operation()
            elif user_input == 3:
                print(f"ACCOUNT BALANCE: ${account.balance}")
                return self.extra_operation()
            elif user_input == 4:
                print("Disconnected. Thank you for using our services.")
                return

    def extra_operation(self):
        print('''1 - BACK TO MAIN MENU\n2 - EXIT''')
        menu_or_out = int(input("Please choose one of the options according to its NUMBER: "))
        if menu_or_out == 1:
            return self.show_account_menu(self.account)
        elif menu_or_out == 2:
            print("Disconnected. Thank you for using our services.")
            return
        else:
            print("Invalid entry. Disconnected.")


account1 = BankAccount(2000,'ronny', 'ronny1234')
account2 = MinimumBalanceAccount(800,'lena', '1910')
accounts = [account1, account2, newbank]
atm = ATM(accounts, 3)
atm.show_main_menu()





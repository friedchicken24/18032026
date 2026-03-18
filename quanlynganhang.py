class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number
        self.balance = balance

    @property
    def account_number(self):
        return self._account_number

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Đã nạp {amount} vào tài khoản. Số dư mới: {self.balance}")
        else:
            print("Số tiền nạp phải lớn hơn 0.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Giao dịch thất bại: Số dư không đủ!")
        elif amount <= 0:
            print("Số tiền rút phải lớn hơn 0. =((( ")
        else:
            self.balance -= amount
            print(f"Đã rút {amount} khỏi tài khoản. Số dư mới: {self.balance}")

    def get_balance(self):
        return self.balance


my_account = BankAccount("123456789", 1000)

print(f"Số tài khoản: {my_account.account_number}")
print(f"Số dư ban đầu: {my_account.get_balance()}")

my_account.deposit(500)
my_account.withdraw(200)
my_account.withdraw(2000) 
print(f"Số dư hiện tại: {my_account.get_balance()}")
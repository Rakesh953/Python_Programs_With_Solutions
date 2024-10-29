class Bank:
    Bank_Name = 'SBI'
    Branch_Name = 'Marthahalli'
    IFSC_Code = 'SBI00891S160'
    base_ROI = 0.06  # Changed the variable name to base_ROI
    def __init__(self, Name, ACCNO, Mno, Bal, Pin):
        self.Name = Name
        self.ACCNO = ACCNO
        self.Mno = Mno
        self.Bal = Bal
        self.Pin = Pin
    @staticmethod
    def validate():
        try:
            return int(input('Enter 4 Digit Pin: '))
        except ValueError:
            print('Invalid Input. Please enter a 4 digit Pin.')
            return Bank.validate()
    def withdraw(self):
        if self.Pin == self.validate():
            amount = int(input('Enter Your Amount: '))
            if self.Bal >= amount:
                self.Bal -= amount
                print(f'Withdrawal successful. Balance: {self.Bal}')
            else:
                print('Insufficient Balance...')
        else:
            print('Incorrect Pin...')
    def deposit(self):
        if self.Pin == self.validate():
            amount = int(input('Enter Your Amount: '))
            self.Bal += amount
            print(f'Deposit successful. Balance: {self.Bal}')
        else:
            print('Incorrect Pin...')
    def check_balance(self):
        if self.Pin == self.validate():
            print(f'Your Balance: {self.Bal}')
        else:
            print('Incorrect Pin...')
    def change_pin(self):
        if self.Pin == self.validate():
            new_pin = int(input('Enter the new Pin: '))
            re_enter_pin = int(input('Re-Enter The Pin: '))
            if new_pin == re_enter_pin:
                self.Pin = new_pin  # Corrected variable name to assign new pin
                print('Pin Updated Successfully...')
            else:
                print('Re-entered Pin does not match. Please try again...')
        else:
            print('Incorrect Pin...')
    @classmethod
    def change_ROI(cls):
        try:
            cls.base_ROI = float(input('Enter New Interest Rate: '))
        except ValueError:
            print('Invalid Input. Please enter a valid interest rate.')
    def transfer_money(self, target_account, amount):
        if self.Pin == self.validate():
            if self.Bal >= amount:
                self.Bal -= amount
                target_account.Bal += amount
                print(f'Transfer successful. Balance: {self.Bal}')
            else:
                print('Insufficient Balance...')
        else:
            print('Incorrect Pin...')
    def display_info(self):
        print(f"Account Holder: {self.Name}")
        print(f"Account Number: {self.ACCNO}")
        print(f"Phone Number: {self.Mno}")
        print(f"Current Balance: {self.Bal}")
    def calculate_interest(self):
        interest = self.Bal * Bank.base_ROI
        print(f"Interest earned: {interest}")

# Sample usage:
B1 = Bank('Rakesh Meher', 466277011000841, 9078896543, 5000, 1111)
B2 = Bank('Siva Khamari', 366267011090841, 8578892543, 6000, 2222)
# B1.withdraw()
# Other method calls and functionalities can be added here...
B1.calculate_interest()

class Bank:
    loan = 0
    def __init__(self,user,balance):
        self.user=user
        self.__balance=balance

    def check(self):
        return self.__balance

    def deposit(self,money):
        self.__balance += money
        return self.__balance

    def withdraw(self,money):
        if money>self.__balance:
            print("Invalid you cannot withdraw more than your balance.")
        elif money<0:
            print("Invalid you cannot withdraw negative cash.")
        else:
            self.__balance -= money
            return self.__balance


per1 = Bank("0000804036201154",500)
print("*"*20+" Bank "+"*"*20)
print(f"User: {per1.user}")
while True:
    choice=int(input("\n1.Check Balance \n2.Deposit Money \n3.Withdraw Money \n4.Display Loan \n5.Take Loan \n6.Pay Loan \n7.Exit \nEnter your choice(1-7) :"))

    if choice==1:
        print(f"Total balance: {per1.check()}")

    elif choice==2:
        money=int(input("Enter amount to deposit: "))
        if money>0:
            print(f"Total Balance: {per1.deposit(money)}")
        else:
            print(f"Total balance: {per1.check()}")

    elif choice==3:
        money = int(input("Enter amount to withdraw: "))
        if money>0:
            print(f"Total Balance: {per1.withdraw(money)}")
        else:
            print(f"Total balance: {per1.check()}")
    elif choice==4:
        print(f"Total loan: {per1.loan}")

    elif choice==5:
        money = float(input("Enter amount to take the loan: "))
        limit = 1.5 * per1.check()

        if money > 0 and money <= limit:
            per1.loan += money
            print(f"Total loan= {per1.loan}")
        else:
            print(f"You have limit of: {limit}")

    elif choice==6:
        loan = float(input("Enter amount to pay the loan: "))
        if loan<per1.loan and loan>0:
            per1.loan -= loan
        else:
            print("Loan payment error please enter valid amount")

    elif choice == 7:
        exit()
    else:
        print("Please enter valid number from (1-5)")

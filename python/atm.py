class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: $"))
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. Your new balance is: ${self.balance}")

    def deposit(self):
        amount = float(input("Enter the amount to deposit: $"))
        self.balance += amount
        print(f"Deposit successful. Your new balance is: ${self.balance}")


def main():
    atm = ATM(1000)  # Initialize ATM with a balance of $1000

    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            atm.withdraw()
        elif choice == "3":
            atm.deposit()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()
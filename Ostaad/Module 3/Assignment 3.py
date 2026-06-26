class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance      

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance!")

    def deposit(self, amount, note=""):
        self.__balance += amount

        if note:
            print(f"Deposited {amount} Taka ({note})")
        else:
            print(f"Deposited {amount} Taka")


class Sports:
    def play(self):
        print("Playing football.")


class Music:
    def sing(self):
        print("Singing a song.")


class StudentActivity(Sports, Music):
    def introduce(self):
        print("I participate in sports and music.")


account = BankAccount("Ayshi", 5000)

print("Current Balance:", account.get_balance())

account.deposit(1000)
account.deposit(500, "Scholarship")

print("Updated Balance:", account.get_balance())

account.set_balance(8000)
print("New Balance:", account.get_balance())


print()

activity = StudentActivity()

activity.introduce()
activity.play()
activity.sing()
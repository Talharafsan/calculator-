def get_number(text):
    while True:
        try:
            return float(input(text))
        except ValueError:
            print("Invalid input! Enter a valid number otherwise cannot run ")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


class Calculator:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b

    def menu(self):
        print("\n**************** MENU ****************")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        print("**************************************")

    def run_menu(self):
        while True:
            self.menu()
            choice = input("Enter your choice [1-5]: ")

            if choice == '5':
                print("Exiting from the calculator...")
                break

            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice! Try again.")
                continue

            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == '1':
                result = self.add(num1, num2)
                print(f"{num1} + {num2} = {result}")

            elif choice == '2':
                result = self.sub(num1, num2)
                print(f"{num1} - {num2} = {result}")

            elif choice == '3':
                result = self.multiply(num1, num2)
                print(f"{num1} * {num2} = {result}")

            elif choice == '4':
                result = self.divide(num1, num2)
                print(f"{num1} / {num2} = {result}")

calc = Calculator()
calc.run_menu()

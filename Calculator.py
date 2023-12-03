# Calculator
#The objective of this project is to design and develop a calculator application in Python that
#allows users to perform basic arithmetic operations such as addition, subtraction,
#multiplication, and division. The application should provide a user-friendly interface and
#accurate calculations.

# Normal Task

class Calculator:
 def __init__(self):
 self.result = 0
 def add(self, number):
 self.result += number
 return self.result
 def subtract(self, number):
 self.result -= number
 return self.result
 def multiply(self, number):
 self.result *= number
 return self.result
 def divide(self, number):
 if number == 0:
 raise ValueError("Division by zero is not allowed")
 self.result /= number
 return self.result
def start_calculator():
 calculator = Calculator()
 while True:
 print("\nPlease choose an operation:")
 print("1. Add")
 print("2. Subtract")
 print("3. Multiply")
 print("4. Divide")
 print("5. Exit")
 choice = input("Enter your choice (1/2/3/4/5): ")
 if choice == '5':
 break
 number = float(input("Enter a number: "))
 if choice == '1':
 print(f"Result: {calculator.add(number)}")
 elif choice == '2':
 print(f"Result: {calculator.subtract(number)}")
 elif choice == '3':
 print(f"Result: {calculator.multiply(number)}")
 elif choice == '4':
 try:
 print(f"Result: {calculator.divide(number)}")
 except ValueError as e:
 print(e)
 else:
 print("Invalid input!")
if __name__ == "__main__":
 start_calculator()

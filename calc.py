import os
import time


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


os.system('cls' if os.name == 'nt' else 'clear')

print("\033[91m {}\033[00m".format("© raven.ovh | 2023"))
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4): ")
os.system('cls' if os.name == 'nt' else 'clear')
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
os.system('cls' if os.name == 'nt' else 'clear')
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
    time.sleep(5)
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
    time.sleep(5)
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
    time.sleep(5)
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
    time.sleep(5)
else:
    print("Invalid input")

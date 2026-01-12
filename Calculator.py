import math

print("---- Calculator ----")
num1 = float(input("Enter First Number : "))
num2 = float(input("Enter Second Number : "))

print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")

choice = int(input("Enter a choice : "))
print("---  Result  ---")

if choice == 1:
    print(f"The addition of {num1} and {num2} is :",(num1 + num2))
elif choice == 2:
    print(f"The Substraction of {num1} and {num2} is :",(num1 - num2))
elif choice == 3:
    print(f"The Multiplication of {num1} and {num2} is :",(num1 * num2))
elif choice == 4:
    if num2 <= 0:
        print("Cannot be divided by zero!")
    else :
        print(f"The Division of {num1} and {num2} is : ",(num1 / num2))
elif choice == 5:
    print("--- Exited Sucessfully! ---")
else:
    print("Please enter a valid choice!")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose Operation:")
print(" Add (+)")
print(" Sub (-)")
print(" Mul (*)")
print(" Div (/)")

choice = input("Enter choice (1-4): ")

if choice == "Add":
    print("Result:", num1 + num2)

elif choice == "Sub":
    print("Result:", num1 - num2)

elif choice == "Mul":
    print("Result:", num1 * num2)

elif choice == "Div":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero!")

else:
    print("Invalid choice")

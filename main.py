"""
main.py

Main program to demonstrate the calculator functions.
Each student implements one function (add, sub, mul, div)
inside calculator/operations.py according to their assigned role.
"""

from calculator.operations import add, sub, mul, div


def main():
    print("=== Team Calculator ===")
    print("Available operations: add, sub, mul, div")
    print("Type 'exit' to quit.\n")

    while True:
        operation = input("Choose operation: ").strip().lower()
        if operation == "exit":
            print("Goodbye!")
            break

        if operation not in ("add", "sub", "mul", "div"):
            print("Invalid operation. Try again.\n")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.\n")
            continue

        try:
            if operation == "add":
                result = add(a, b)
                symbol = "+"
            elif operation == "sub":
                result = sub(a, b)
                symbol = "-"
            elif operation == "mul":
                result = mul(a, b)
                symbol = "*"
            elif operation == "div":
                result = div(a, b)
                symbol = "/"

            print(f"\nOperation: {operation.upper()}")
            print(f"Calculation: {a} {symbol} {b} = {result}\n")

        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.\n")
        except Exception as e:
            print(f"Unexpected error: {e}\n")


if __name__ == "__main__":
    main()

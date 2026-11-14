"""Simple calculator - a small command-line program."""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return a times b."""
    return a * b


def divide(a, b):
    """Return a divided by b. Raise ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


OPERATIONS = {
    "1": ("+", add),
    "2": ("-", subtract),
    "3": ("*", multiply),
    "4": ("/", divide),
}


def main():
    print("=== Simple Calculator ===")
    while True:
        print("\n1) Add  2) Subtract  3) Multiply  4) Divide  0) Exit")
        choice = input("Choose an operation: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        if choice not in OPERATIONS:
            print("Invalid choice.")
            continue
        a = float(input("First number: "))
        b = float(input("Second number: "))
        symbol, func = OPERATIONS[choice]
        try:
            print(f"{a} {symbol} {b} = {func(a, b)}")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()

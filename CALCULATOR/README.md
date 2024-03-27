# Calculator

This is a simple calculator program written in Python. It allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Features

- **Addition:** Adds two numbers together.
- **Subtraction:** Subtracts one number from another.
- **Multiplication:** Multiplies two numbers.
- **Division:** Divides one number by another. Division by zero is handled, and an error message is displayed in such cases.

## How to Use

1. **Clone the repository:**

   ```git clone <repository-url>```

2. **Navigate to the project directory:**

    ```cd calculator```

3. **Run the calculator program:**

```python calculator.py```

## Usage Example

# Perform addition
result = add(5, 3)
print("5 + 3 =", result)

# Perform subtraction
result = subtract(10, 4)
print("10 - 4 =", result)

# Perform multiplication
result = multiply(6, 2)
print("6 * 2 =", result)

# Perform division
result = divide(8, 2)
print("8 / 2 =", result)

## Error Handling
The program handles division by zero gracefully. If the user attempts to divide by zero, an error message is displayed, and the operation is aborted.

## Example of division by zero
result = divide(5, 0)
print(result)  # Output: "Error: Cannot divide by zero."

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.


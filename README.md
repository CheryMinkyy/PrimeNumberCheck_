# Prime Number Checker

This Python program checks if a given number is prime. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

## Key Concepts

- **Control Structures:** Using `if` statements and loops to implement the prime-checking logic.
- **Mathematical Operations:** Utilizing modular arithmetic and square root optimizations to improve efficiency.

## Requirements

- Python 3.x

## How It Works

1. The program takes an integer input from the user.
2. It checks if the number is less than or equal to 1, as numbers 1 and below are not prime.
3. For numbers greater than 1, the program checks divisibility from 2 up to the square root of the number. This reduces the number of operations required.
4. If the number is divisible by any integer in this range, it is not prime; otherwise, it is prime.

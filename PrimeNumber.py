def is_prime(number):
    # Numbers 1 and 0 are not prime.
    if number <= 1:
        return False
    # Check divisibility up to the square root of the number.
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Take a number from the user and check if it is prime.
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

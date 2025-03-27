#Given a python list [10,501,22,37,100,999,87,351]to count all the prime numbers and create a new python list which will contain all the prime numbers in it?


#count all the prime numbers in a list and create a new list containing those prime numbers, 
# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is a prime number
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# List to hold prime numbers
prime_numbers = [num for num in numbers if is_prime(num)]

# Output the results
print("Prime numbers:", prime_numbers)
print("Count of prime numbers:", len(prime_numbers))

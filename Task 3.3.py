#Given a python list [10,501,22,37,100,999,87,351]Find out how many numbers are there in the given python list which are happy numbers?
#To determine how many numbers in the given Python list are happy numbers, we first need to understand what a happy number is:
#A happy number is defined by the following process:
##Start with any positive integer.
#Replace the number with the sum of the squares of its digits.
#Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle that does not include 1.
#Numbers for which this process ends in 1 are called happy numbers.
    
# Function to check if a number is a happy number
def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1
# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
# List to hold happy numbers
happy_numbers = [num for num in numbers if is_happy_number(num)]
# Output the results
print("Happy numbers:", happy_numbers)
print("Count of happy numbers:", len(happy_numbers))

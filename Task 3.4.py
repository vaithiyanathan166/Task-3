#4 ) write a python program to find the sum of the first and last digit of an integer?
# Function to calculate the sum of the first and last digit
def sum_first_last_digit(number):
    # Convert the number to a string to easily access the digits
    num_str = str(abs(number))  # Use abs() to handle negative numbers
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])
    return first_digit + last_digit

# Example usage
number = int(input("Enter an integer: "))
result = sum_first_last_digit(number)
print(f"The sum of the first and last digit of {number} is: {result}")

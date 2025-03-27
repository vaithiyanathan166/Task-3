#python list [10,501,22,37,100,999,87,351] task is to create two list one which have all the even numbers and another list which will have all the odd numbers in it?



# Original list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Lists to hold even and odd numbers
even_numbers = []
odd_numbers = []

# Loop through the list and separate even and odd numbers
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# Print the results
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

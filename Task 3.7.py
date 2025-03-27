#7 ) write a python program to find the first non repeating elements in a given list of integers?

def first_non_repeating_element(nums):
    # Count occurrences of each element using a dictionary
    count_dict = {}

    for num in nums:
        count_dict[num] = count_dict.get(num, 0) + 1

    # Find the first element that appears only once
    for num in nums:
        if count_dict[num] == 1:
            return num

    return None  # If all elements repeat

# Example usage
nums = [4, 5, 1, 2, 0, 4, 2, 5]
result = first_non_repeating_element(nums)

if result is not None:
    print(f"The first non-repeating element is: {result}")
else:
    print("There are no non-repeating elements in the list.")

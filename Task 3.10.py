#10 ) Given a list [4,2,-3,1,6]write a python program to find if there is a sub list with sum equal to zero ?

def has_zero_sum_sublist(nums):
    # Initialize a set to store the cumulative sums
    seen_sums = set()
    
    # Initialize the cumulative sum
    current_sum = 0
    
    for num in nums:
        # Update the cumulative sum
        current_sum += num
        
        # Check if the cumulative sum is zero or if we've seen this sum before
        if current_sum == 0 or current_sum in seen_sums:
            return True
        
        # Add the current cumulative sum to the set
        seen_sums.add(current_sum)
    
    return False

# Example usage
nums = [4, 2, -3, 1, 6]
result = has_zero_sum_sublist(nums)

if result:
    print("There is a sublist with a sum of zero.")
else:
    print("There is no sublist with a sum of zero.")

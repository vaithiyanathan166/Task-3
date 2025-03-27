#9 ) you have been give a python list [10,20,30,9] and a value of 59.write python program to find the triplet in the list whose sum is equal to the given value?

#A  triplet in a list whose sum equals a given value,  use a combination of sorting and the two-pointer technique for efficiency. 

def find_triplet_with_sum(nums, target):
    # Sort the list
    nums.sort()
    
    n = len(nums)
    
    # Iterate over the list
    for i in range(n - 2):
        left, right = i + 1, n - 1
        
        # Use two-pointer approach to find the other two numbers
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == target:
                return (nums[i], nums[left], nums[right])
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return None  # If no triplet is found

# Example usage
nums = [10, 20, 30, 9]
target = 59
result = find_triplet_with_sum(nums, target)

if result:
    print(f"Triplet with sum {target} is: {result}")
else:
    print(f"No triplet with sum {target} found.")

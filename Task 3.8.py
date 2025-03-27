#8 ) write a python program to find the minimum element in a rated and sorted list?

def find_min_in_rotated_sorted_list(nums):
    # If the list is empty, return None
    if not nums:
        return None
    
    left, right = 0, len(nums) - 1
    
    # If the list is already sorted (not rotated), return the first element
    if nums[left] <= nums[right]:
        return nums[left]

    while left <= right:
        mid = (left + right) // 2
        
        # Check if mid is the pivot (minimum element)
        if mid < right and nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        
        if mid > left and nums[mid] < nums[mid - 1]:
            return nums[mid]
        
        # Narrow the search space
        if nums[mid] > nums[right]:  # Minimum must be in the right half
            left = mid + 1
        else:  # Minimum must be in the left half
            right = mid - 1

    return None  # If the list is invalid

# Example usage
rotated_sorted_list = [4, 5, 6, 7, 0, 1, 2]
result = find_min_in_rotated_sorted_list(rotated_sorted_list)

if result is not None:
    print(f"The minimum element in the rotated sorted list is: {result}")
else:
    print("The list is empty or invalid.")

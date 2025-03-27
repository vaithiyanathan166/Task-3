#6 ) you have been given three lists .your task is to find the duplicates in the three lists 
# write a python program for the same you can use your own python lists ?
# Example lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
list3 = [5, 6, 10, 11, 12]

# Find duplicates present in all three lists
duplicates = set(list1) & set(list2) & set(list3)

# Print results
print("Duplicates in all three lists:", list(duplicates))

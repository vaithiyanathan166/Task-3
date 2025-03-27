#5 ) you have been given a list of N integers which represents the number of mangoes in a bag each bag has a variable number of mangaoes .there are m student in a guvi class your task is to distribute the mangoes in such a way that each student gets one bag the difference between the number of mangoes in a bag with maximum mangoes given to the student is maximum ?

#Sort the list of mangoes.

#Distribute the mangoes to the students in such a way that the first student gets the smallest bag and the last student gets the largest bag. 

#This ensures that the difference between the maximum and minimum is maximized.

#Calculate the difference between the number of mangoes in the bag with the maximum and minimum mangoes.


def max_mango_difference(mangoes, m):
    # Sort the list of mangoes
    mangoes.sort()

    # If students are more than available bags, return -1
    if m > len(mangoes):
        return -1  # Not enough bags to distribute

    # Get the maximum difference within the first `m` selected bags
    max_diff = mangoes[m - 1] - mangoes[0]

    return max_diff

# Example usage
mangoes = [10, 20, 30, 50, 70, 100, 200]
m = 3  # Number of students
result = max_mango_difference(mangoes, m)
print(f"The maximum difference in mangoes distributed to the students is: {result}")

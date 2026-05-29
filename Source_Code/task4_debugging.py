"""
Task 4: Corrected Code After Debugging
"""

# Original Buggy Code:
# numbers = [1,2,3,4,5] 
# sum = 0 
# for i in range(0, len(numbers)+1): 
#     sum += numbers[i] 
# print("Average:", sum/0) 

# ----------------------------------------
# CORRECTED VERSION
# ----------------------------------------

numbers = [1, 2, 3, 4, 5]

# Changed variable name from 'sum' to 'total_sum' to avoid overriding Python's built-in sum() function.
total_sum = 0 

# Fixed IndexError: changed range to stop at len(numbers), not len(numbers) + 1
for i in range(len(numbers)): 
    total_sum += numbers[i] 

# Fixed ZeroDivisionError & Logical Error: Divide by len(numbers) instead of 0 to get the average
if len(numbers) > 0:
    average = total_sum / len(numbers)
    print("Average:", average)
else:
    print("List is empty, cannot calculate average.")

# Alternative Pythonic way using built-ins (AI suggestion):
# print("Average:", sum(numbers) / len(numbers) if numbers else 0)

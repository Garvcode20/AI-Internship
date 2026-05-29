"""
Task 5: Code Optimization Challenge
Problem: Find if there are any two numbers in a list that add up to a specific target. (Two Sum Problem)
"""
import time
import random

# ---------------------------------------------------------
# 1. Before Optimization: Brute Force (Nested Loops)
# ---------------------------------------------------------
def two_sum_brute_force(nums, target):
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# ---------------------------------------------------------
# 2. After Optimization: Hash Map (Dictionary)
# ---------------------------------------------------------
def two_sum_optimized(nums, target):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    num_map = {} # Value -> Index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

# ---------------------------------------------------------
# Testing & Performance Comparison
# ---------------------------------------------------------
if __name__ == "__main__":
    # Generate a large dataset for testing
    large_list = list(range(1, 10000))
    target_value = 19997 # Requires finding elements near the end of the list

    print(f"List size: {len(large_list)} elements")
    
    # Test Brute Force
    start_time = time.time()
    res1 = two_sum_brute_force(large_list, target_value)
    end_time = time.time()
    print(f"Brute Force Result: {res1}, Time taken: {(end_time - start_time):.6f} seconds")

    # Test Optimized
    start_time = time.time()
    res2 = two_sum_optimized(large_list, target_value)
    end_time = time.time()
    print(f"Optimized Result: {res2}, Time taken: {(end_time - start_time):.6f} seconds")

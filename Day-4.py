# Problem2: Count Number of Nice Subarrays
#
# Problem:
# Given an array of integers and an integer k, return the number of subarrays with exactly k odd numbers.
#
# Test Case 1
# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: Subarrays [1,1,2,1] and [1,2,1,1]
#
# Test Case 2
# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There are no odd numbers, so no subarrays with exactly 1 odd number.
#
# Test Case 3
# Input: nums = [2,2,2,1,2,2,1,2,2,2,1], k = 3
# Output: 3
# Explanation: Possible valid subarrays:
#    - [2,2,2,1,2,2,1]
#    - [2,2,1,2,2,2,1]
#    - [1,2,2,2,1]

#program:
nums = [1,1,2,1,1]
k = 3
count = 0
for i in range(len(nums)):
    odd = 0
    for j in range(i, len(nums)):
        if nums[j] % 2 != 0:
            odd += 1
        if odd == k:
            count += 1
        elif odd > k:
            break
print("Number of subarrays:",count)


# 1. Problem Description
# You are given:
# • An array chocolates[] where each element represents the number of chocolate bars in a set.
# • An integer k representing the maximum number of hours available.
#
# You eat chocolates at a constant rate of r bars per hour. 
# Eating part of a chocolate bar in an hour still counts as a full hour (i.e., the time is rounded up).
#
# Your task is to determine the minimum integer value of r such that 
# you can finish all the chocolates in k hours or less.
#
# ---------------------------------------------------
# Example:
# Input:
# chocolates = [6, 3, 4]  
# k = 5
#
# Explanation:
# If r = 3:
#   • First set: ceil(6 / 3) = 2 hours
#   • Second set: ceil(3 / 3) = 1 hour
#   • Third set: ceil(4 / 3) = 2 hours
#   • Total = 2 + 1 + 2 = 5 hours (equals k) ✅
#
# So, the output is:
# 3

#code:
import math

def min_eating_rate(chocolates, k):
    for r in range(1, max(chocolates) + 1):
        hours = 0
        for c in chocolates:
            hours += math.ceil(c / r)
        if hours <= k:
            return r

chocolates = [6, 3, 4]
k = 5
result = min_eating_rate(chocolates, k)
print(result)

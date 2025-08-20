# Problem Description
# You are given an n × m grid representing a forest. 
# Each cell contains one of the following:
# 0 → No tree (empty land).
# 1 → Tree is not on fire.
# 2 → Tree is on fire.
#
# Each day, the fire spreads from any burning tree (2) to its adjacent trees 
# in the top, bottom, left, and right directions. 
# Fire does not spread through empty land (0).
#
# Your task is to determine the minimum number of days required 
# for all trees in the forest to be on fire. 
# If it’s impossible for all trees to catch fire, return -1.
#
# ---------------------------------------------------
# Example 1:
# Input:
# forest = [
#     [1, 1, 1],
#     [1, 2, 1],
#     [1, 1, 1]
# ]
#
# Explanation:
# Day 0:
# [1, 1, 1]  
# [1, 2, 1]  
# [1, 1, 1]  
#
#•	Day 1:
[1, 2, 1]  
[2, 2, 2]  
[1, 2, 1]  
# Day 2:
# [2, 2, 2]  
# [2, 2, 2]  
# [2, 2, 2]  
# Output:
# 2

#code:
def minDaysToBurnForest(forest):
    n = len(forest)
    m = len(forest[0])
    days = 0

    while True:
        # list to store which trees will catch fire today
        new_fire = []

        for i in range(n):
            for j in range(m):
                if forest[i][j] == 2:   # burning tree
                    # check up
                    if i > 0 and forest[i-1][j] == 1:
                        new_fire.append((i-1, j))
                    # check down
                    if i < n-1 and forest[i+1][j] == 1:
                        new_fire.append((i+1, j))
                    # check left
                    if j > 0 and forest[i][j-1] == 1:
                        new_fire.append((i, j-1))
                    # check right
                    if j < m-1 and forest[i][j+1] == 1:
                        new_fire.append((i, j+1))

        # if no new fire today → stop
        if not new_fire:
            break

        # burn the new trees
        for x, y in new_fire:
            forest[x][y] = 2

        days += 1   # one day passed

    # check if any tree left unburned
    for row in forest:
        if 1 in row:
            return -1
    return days
m=int(input("enter number of rows:"))
n=int(input("enter number of columns:"))
forest=[]
for i in range(m):
    row=list(map(int,input().split()))
    forest.append(row)
result = minDaysToBurnForest(forest)
print(result)

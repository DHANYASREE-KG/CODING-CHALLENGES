# Problem Description
# You are given two arrays:
# • jobs[] → Each element represents the difficulty level of a job.
# • employees[] → Each element represents the skill level of an employee.
# 
# A job can be done by an employee if the employee’s skill level is 
# greater than or equal to the job’s difficulty. 
# Each employee can do at most one job, 
# and each job can be assigned to at most one employee.
# 
# Your task is to determine the maximum number of jobs that can be completed.
# 
# Example:
# Input:
# jobs = [4, 6, 9, 13]  
# employees = [1, 5, 10, 7]
# 
# Explanation:
# One possible optimal assignment is:
# • Employee with skill 10 → Job with difficulty 9 ✅
# • Employee with skill 7 → Job with difficulty 6 ✅
# • Employee with skill 5 → Job with difficulty 4 ✅
# Jobs done = 3.
# 
# Output:
# 3


#code:
jobs=[4,6,9,13]
employees=[1,5,10,7]
def max_1(jobs,employees):
    jobs.sort()
    employees.sort()
    i=0
    j=0
    count=0
    n,m=len(jobs),len(employees)
    while i<n and j<m:
        if employees[j]>=jobs[i]:
            i+=1
            j+=1
            count+=1
        else:
            j+=1
    return count
print(max_1(jobs,employees))

#or
count = 0
for emp in employees:
    for j in jobs:
        if emp >= j:     # employee skill >= job difficulty
            count += 1
            jobs.remove(j)   # remove job once assigned
            break


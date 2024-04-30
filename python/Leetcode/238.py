"""  product of array except self"""

nums = [1,2,3,4]

lennums = len(nums)
product = [1] * lennums

""" parts of lpart"""
for i in range(1, lennums):
    product[i] = product[i-1] * nums[i-1]


""" including right part multiplication """
right = nums[-1]

for i in range(lennums-2,-1,-1):
    product[i]*=right
    right*=nums[i]

print("product", product)
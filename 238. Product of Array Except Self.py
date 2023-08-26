"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

def ProductExceptSelf(nums):
    n = len(nums)

    Prefix_Products = [1] * n
    Suffix_Products = [1] * n

    Prefix_Product = 1
    for i in range(n):
        Prefix_Products [i] = Prefix_Product
        Prefix_Product *= nums[i]

    Suffix_Product = 1
    for i in range(n-1, -1, -1):
        Suffix_Products[i] = Suffix_Product
        Suffix_Product *= nums[i]

    answer = [Prefix_Products[i] * Suffix_Products[i] for i in range(n)]

    return answer


num1 = [1,2,3,4]
num2 = [-1, 1, 0, -3, 3]

print(ProductExceptSelf(num1))
print(ProductExceptSelf(num2))

Q- You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]
 

Constraints:

2 <= nums.length <= 104
1 <= nums[i] <= 104

Solutions- 
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        xor_sum = 0
        for i in range(1, n+1):
            xor_sum ^= i
            xor_sum ^= nums[i-1]
        rightmost_set_bit = xor_sum & ~(xor_sum-1)
        xor_group1 = xor_group2 = 0
        for i in range(1, n+1):
            if i & rightmost_set_bit:
                xor_group1 ^= i
            else:
                xor_group2 ^= i
            if nums[i-1] & rightmost_set_bit:
                xor_group1 ^= nums[i-1]
            else:
                xor_group2 ^= nums[i-1]
        for num in nums:
            if num == xor_group1:
                return [num, xor_group2]
            elif num == xor_group2:
                return [num, xor_group1]

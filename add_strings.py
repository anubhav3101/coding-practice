# Q-415 
# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

# Example 1:

# Input: num1 = "11", num2 = "123"
# Output: "134"
# Example 2:

# Input: num1 = "456", num2 = "77"
# Output: "533"
# Example 3:

# Input: num1 = "0", num2 = "0"
# Output: "0"
 

# Constraints:

# 1 <= num1.length, num2.length <= 104
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.

# Answer- 

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        dic = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9 }

        ans = ''
        c = 0

        while num1 or num2 or c:
            s = c
            if num1:
                s += dic[num1[-1]]
                num1 = num1[:-1]
            if num2:
                s += dic[num2[-1]]
                num2 = num2[:-1]
       
            c = s // 10
            ans = str(s %10) + ans

        return ans
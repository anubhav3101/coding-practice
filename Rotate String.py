Q- Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
 

Constraints:

1 <= s.length, goal.length <= 100
s and goal consist of lowercase English letters.

Solution- 

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # print(s[::-1])
        # return
        n = len(s)
        for i in range(n):
            tmp1 = s[:n-i]
            tmp2 = s[n-i:]
            tmp = tmp2 + tmp1
            if tmp == goal:
                return True
        return False
        

Q- Valid Palindrome II
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.

Solution- 
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i,j = 0, len(s)-1
        
        while i < j:
            if s[i] != s[j]:
                return s[i+1:j+1] == s[i+1:j+1][::-1] or s[i:j] == s[i:j][::-1]
            i += 1
            j -= 1
        
        return True

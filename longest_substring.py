'''
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = defaultdict(int)
        left = right = ans = 0
        
        for char in s:
            curr[char] += 1
            while curr[char] > 1:
                curr[s[left]] -= 1
                if curr[s[left]] == 0:
                    del curr[s[left]]
                left += 1
            
            right += 1
            ans = max(ans, right - left)
        
        return ans
            
        
                    
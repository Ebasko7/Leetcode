"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 


"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = "balloon"
        bdict = {}
        tdict = {}
        mins = []

        for letter in balloon:
            if letter not in bdict:
                bdict[letter] = 1
            else:
                bdict[letter] += 1

        for letter in text:
            if letter in balloon and letter not in tdict:
                tdict[letter] = 1
            elif letter in balloon and letter in tdict:
                tdict[letter] += 1

        for key, val in tdict.items():
            if key == "b" or key == "a" or key == "n":
                mins.append(val)
            if key == "l" or key == "o":
                mins.append(val / 2)

        if len(tdict) < len(bdict):
            return 0

        return int(min(mins))

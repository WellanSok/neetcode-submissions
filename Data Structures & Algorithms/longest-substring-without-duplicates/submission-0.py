class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        res = 0
        chars = set()
        for end in range(len(s)):
            while s[end] in chars:
                chars.remove(s[start])
                start +=1
            chars.add(s[end])
            res = max(res,end-start+1)
        return res

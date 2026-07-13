class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqMap1 = {}
        freqMap2 = {}
        for st in s :
            freqMap1[st] = freqMap1.get(st,0) + 1
        for st in t :
            freqMap2[st] = freqMap2.get(st,0) + 1
        return freqMap1 == freqMap2
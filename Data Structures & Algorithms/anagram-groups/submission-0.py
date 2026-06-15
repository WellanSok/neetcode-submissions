class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for c in word:
                freq[ord(c)-ord('a')] += 1 
            sol[tuple(freq)].append(word)
        return list(sol.values())
            
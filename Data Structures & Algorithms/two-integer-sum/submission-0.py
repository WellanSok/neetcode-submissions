class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            compliment = target-nums[i]
            if compliment in freq:
                return [freq[compliment],i]
            else:
                freq[nums[i]] = i

        
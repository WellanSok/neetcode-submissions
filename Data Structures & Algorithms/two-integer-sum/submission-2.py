class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in compliments:
                return [compliments[comp],i]
            else:
                compliments[nums[i]] = i
                
            
        
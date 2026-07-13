class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0 
        dayOne , dayTwo = 0,1
        while dayTwo < len(prices):
            if prices[dayTwo] > prices[dayOne]:
                prof = prices[dayTwo]-prices[dayOne]
                maxProf = max(prof,maxProf)
            else:
                dayOne = dayTwo
            dayTwo +=1
        return maxProf


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        
        summ = 0
        ans = -inf
        for num in nums:

            summ += num
            ans = max(ans, summ)
            summ = max(summ, 0)
        
        return ans
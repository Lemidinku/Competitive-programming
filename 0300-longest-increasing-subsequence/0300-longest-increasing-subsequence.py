class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        @cache
        def findSub(i):
            if i==n-1:
                return 1
            
            ans = 0
            for j in range(i+1,n):
                if nums[j] > nums[i]:
                    ans = max(ans, findSub(j))

            return ans +1

        
        ans = 0
        for i in range(n):
            ans = max(ans,findSub(i))
        
        return ans
            
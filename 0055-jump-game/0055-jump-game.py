class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        steps =nums[0]
        i = 1
        while i<n and steps:
            
            steps = max(steps-1,nums[i])
            i+=1

        
        return i==n

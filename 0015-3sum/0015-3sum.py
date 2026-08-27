class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []
        for i in range(n-2):
            if i>0 and nums[i-1]==nums[i]: continue
            target = -nums[i]
            left = i+1
            right = n-1
            while left<right:
                if  left>i+1 and nums[left]==nums[left-1]: 
                    left+=1
                    continue
                if  right<n-1 and nums[right]==nums[right+1]: 
                    right-=1
                    continue
                if nums[left]+nums[right]==target:
                    result.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                elif nums[left]+nums[right]<target:
                    left+=1
                else: right-=1
            
        return result
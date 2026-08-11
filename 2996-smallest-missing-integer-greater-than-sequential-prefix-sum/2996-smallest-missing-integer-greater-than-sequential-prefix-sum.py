class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)

        summ = nums[0]
        for i in range(1,n):
            if nums[i] != nums[i-1]+1:
                break
            summ += nums[i]
        
        nums  = set(nums)
        
        for num in range(1,52):
            if num >= summ and num not in nums:
                return num

        return summ
        
    


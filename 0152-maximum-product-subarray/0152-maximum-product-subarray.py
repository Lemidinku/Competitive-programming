class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)


        def getMax(nums):
            prod = 1
            if not len(nums): return -inf
            if len(nums)==1: return nums[0]

            for num in nums:
                prod *= num

            if prod > 0:
                return prod
            
            # remove left-most negative number
            left_removed = prod
            for num in nums:
                left_removed //= num
                if num < 0: break
            
            #remove right-most negative number
            right_removed = prod
            for num in nums[::-1]:
                right_removed //= num
                if num < 0: break
            
            return max(left_removed,right_removed)
        
        start = end = 0
        ans = -inf
        while end< n:
            if not nums[end]:
                ans = max(ans, 0, getMax(nums[start:end]))
                start = end+1
            end += 1
        ans = max(ans, getMax(nums[start: ]))

        
    
        return ans

            

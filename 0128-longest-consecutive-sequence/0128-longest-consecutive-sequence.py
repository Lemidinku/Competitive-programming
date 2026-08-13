class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        ans = 0
        for num in nums_set:
            if num-1 not in nums_set:
                leng = 1
                val = num+1
                while val in nums_set:
                    val +=1
                    leng += 1
                ans = max(ans, leng)
        return ans
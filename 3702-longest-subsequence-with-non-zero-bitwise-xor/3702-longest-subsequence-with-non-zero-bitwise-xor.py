class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        if not sum(nums): return 0

        xor = 0

        for num in nums:
            xor ^= num

        if xor ==0:
            return n-1
        return n

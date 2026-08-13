class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre_prod = [1]
        for num in nums:
            pre_prod.append(pre_prod[-1]*num)

        post_prod = [1]
        for num in nums[::-1]:
            post_prod.append(post_prod[-1]*num)
        post_prod.reverse()

        ans = []
        for i in range(len(nums)):
            val = pre_prod[i]*post_prod[i+1]
            ans.append(val)

        return ans
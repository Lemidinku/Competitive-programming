class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre_prod = [1]
        prod = 1
        for num in nums:
            prod *= num
            pre_prod.append(prod)

        post_prod = [1]
        prod = 1
        for num in nums[::-1]:
            prod *= num

            post_prod.append(prod)
        post_prod.reverse()

        ans = []
        for i in range(len(nums)):
            val = pre_prod[i]*post_prod[i+1]
            ans.append(val)
        print(pre_prod, post_prod)

        return ans
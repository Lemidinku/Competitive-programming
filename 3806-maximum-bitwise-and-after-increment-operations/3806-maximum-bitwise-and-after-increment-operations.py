class Solution:
    def maximumAND(self, nums: List[int], k: int, m: int) -> int:
        # 11
        # 1
        # 01
        
        ans = 0
        for bit in range(31,-1,-1):
            target = ans | (1<<bit)

            costs = []
            for num in nums:
                missing = target & ~num

                curr_cost = 0
                if missing:

                    j = missing.bit_length()
                    mask = (1<<(j))-1
                    curr_cost = (target&mask) - (num&mask)
                
                costs.append(curr_cost)
            costs.sort()
            if sum(costs[:m]) <= k:
                ans = target

        return ans
            
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        @cache
        def represent(num):
            if num == 0: return 0
            ways = inf

            for coin in coins:
                if coin <= num:
                    ways = min(ways, 1+represent(num-coin))
            
            return ways

        ans = represent(amount)
        return -1 if ans == inf else ans

        
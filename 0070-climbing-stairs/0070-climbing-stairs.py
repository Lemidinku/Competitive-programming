class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def climb(num):
            if not num:
                return 1
            if num < 0: 
                return 0
            
            return climb(num-1) + climb(num-2)
        
        return climb(n)
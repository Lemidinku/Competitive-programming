class Solution:
    def checkDivisibility(self, n: int) -> bool:
        
        prod = 1
        summ = 0
        num = n
        while num:
            prod *= num%10
            summ += num%10
            num //=10

        return not ( n%(summ +prod))
        


    
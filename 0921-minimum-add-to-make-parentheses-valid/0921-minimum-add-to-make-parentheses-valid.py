class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        adds = 0
        val = 0

        for char in s:
            if char == "(":
                val +=1
            else:
                val -=1
            if val < 0:
                adds +=1
                val= 0

        return adds +val

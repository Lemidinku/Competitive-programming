class Solution:
    def numDecodings(self, s: str) -> int:
        
        @cache
        def decode(s):
            if not len(s):
                return 1
            if len(s)==1:
                return 1 if s !="0" else 0

            ways = 0

            # separate
            if "0" not in s[:2]:
                ways += decode(s[1:])
            
            if s[0] != "0" and int(s[:2]) <= 26:
                ways += decode(s[2:])
            
            return ways
    
        return decode(s)

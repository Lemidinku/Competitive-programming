class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)
        
        def search(target):
            count = 0
            left = 0
            ans = 0
            for right in range(n):
                if s[right] != target:
                    count +=1
                while count > k:
                    if s[left] != target:
                        count -=1
                    left += 1
                ans = max( ans, right-left+1)

            return ans
        
        ans = 0
        for i in range(26):
            target = chr(65+i)
            ans = max(ans, search(target))

        return ans


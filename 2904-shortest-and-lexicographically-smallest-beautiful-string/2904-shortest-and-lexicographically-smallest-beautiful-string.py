class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)

        leng = inf
        count = 0
        left = 0
        for right in range(n):
            if s[right] == "1":
                count +=1
            while count >= k:

                if count==k:
                    leng = min(leng, right-left+1)
                if s[left] == "1":
                    count -=1
                left+=1
        if leng == inf:
            return ""
        
        ans = "z"
        left,right = 0, leng
        count = Counter(s[:leng])

        if count['1'] == k:
            ans = s[:leng]

        while right < n:
            count[s[left]] -=1
            count[s[right]] +=1

            left +=1
            right +=1

            if count['1'] == k and ans > s[left:right]:
                ans = s[left:right]


        return ans

            
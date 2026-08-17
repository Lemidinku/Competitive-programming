class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        freq = defaultdict(int)
        n = len(s)

        def hasAll():
            for char in count:
                if freq[char] < count[char]:
                    return False
            return True

        minn = inf
        ans = ""
        left = 0
        for right in range(n):

            freq[s[right]] +=1
            while hasAll():
                freq[s[left]] -=1
                if right-left+1 < minn:
                    ans = s[left: right+1]
                    minn = right-left+1
                left +=1

        return ans
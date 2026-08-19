class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        occupied = set((r,c) for r,c in reservedSeats)
        rows = set(r for r,_ in reservedSeats)

        count = (n-len(rows))*2
        for r in rows:
            c = 2
            while c <= 6:
                if not((r,c) in occupied or (r,c+1) in occupied or  (r,c+2) in occupied or (r,c+3) in occupied):
                    count += 1
                    c += 4
                else:
                    c += 2
        return count
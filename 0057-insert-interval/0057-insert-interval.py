class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

        new_intervals = []
        new_left, new_right = newInterval

        inserted = False
        for left,right in intervals:
            if max(new_left,left) <= min(new_right, right):
                left = min(left,new_left)
                right = max(right, new_right)
                inserted = True
            if len(new_intervals):
                prev_left, prev_right = new_intervals[-1]
                if max(prev_left,left) <= min(prev_right, right):
                    left = min(left,prev_left)
                    right = max(right, prev_right)
                    new_intervals.pop()
            new_intervals.append((left,right))
        if not inserted:
            i  = 0
            while i < len(new_intervals):
                x,y = new_intervals[i]
                if x > new_left:
                    break
                i +=1
            new_intervals.insert(i,newInterval)
            
        return new_intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x : (x[0], -x[1]))

        new_intervals = [intervals[0]]
        for left,right  in intervals:
            prev_left, prev_right = new_intervals[-1]
            if max(left, prev_left) <= min(right, prev_right):
                new_intervals[-1][1] = max(right, prev_right)
            else:
                new_intervals.append([left,right])
        return new_intervals


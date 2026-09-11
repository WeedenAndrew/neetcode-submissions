class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        ans = [intervals[0]]

        for start, end in intervals:
            lastEnd = ans[-1][1]

            if start <= lastEnd:
                ans[-1][1] = max(lastEnd, end)
            else:
                ans.append([start, end])

        return ans
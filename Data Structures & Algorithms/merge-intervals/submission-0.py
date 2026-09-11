class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        merged = []

        for x in intervals:
            # A, B: A[0] < B[0]
            # Overlap: A[1] > B[0]
            if not merged or merged[-1][1] < x[0]:
                merged.append(x)
            else:
                merged[-1] = [merged[-1][0], max(merged[-1][1], x[1])]

        return merged
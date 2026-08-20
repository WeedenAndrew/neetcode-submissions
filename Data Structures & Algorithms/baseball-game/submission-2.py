class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []

        for score in operations:
            if score == "+":
                s.append(s[-1] + s[-2])
                continue
            if score == "C":
                s.pop()
                continue
            if score == "D":
                s.append(s[-1] * 2)
                continue
            s.append(int(score))

        return sum(s)
        
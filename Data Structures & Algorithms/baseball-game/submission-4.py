class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []

        for op in operations:
            if op == "+":
                s.append(s[-1] + s[-2])
            elif op == "C":
                s.pop()
            elif op == "D":
                s.append(s[-1] * 2)
            else:
                s.append(int(op))

        return sum(s)
        
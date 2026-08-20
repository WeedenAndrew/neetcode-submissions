class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        ends = {'}': '{',
                ')': '(',
                ']': '['}

        for ch in s:
            if ch not in ends:
                seen.append(ch)
                continue

            if not seen or seen[-1] != ends[ch]:
                return False
            seen.pop()

        return len(seen) == 0
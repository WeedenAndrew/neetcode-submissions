class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c not in close_to_open:
                stack.append(c)
                continue
            
            if not stack or stack[-1] != close_to_open[c]:
                return False
            stack.pop()

        return len(stack) == 0

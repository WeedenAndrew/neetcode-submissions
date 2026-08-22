class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ends = {')': '(',
                ']': '[',
                '}': '{'}

        for char in s:
            if char not in ends:
                stack.append(char)
                continue
                
            if not stack or stack.pop() != ends[char]:
                return False
        
        return stack == []
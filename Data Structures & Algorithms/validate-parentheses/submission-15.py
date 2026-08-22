class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ends = {')': '(',
                ']': '[',
                '}': '{'}

        for char in s:
            if char in ends:
                if stack != [] and stack.pop() == ends[char]:
                    continue
                else:
                    print(stack)
                    return False
            else:
                stack.append(char)
        
        return stack == []
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = list(s.lower().replace('?', "").replace('.', "").replace(',',"").replace(' ', "").replace("'","").replace('"',"").replace(':',""))

        if cleaned == list(reversed(cleaned)):
            return True
        return False
        
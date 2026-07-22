class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1, p2 = 0, 0
        string = ''

        while p1 != len(word1) and p2 != len(word2):
            string = string + word1[p1] + word2[p2]

            p1 += 1
            p2 += 1

            if p1 == len(word1):
                string = string + word2[p2:]

            if p2 == len(word2):
                string = string + word1[p1:]
        
        return string

        
        
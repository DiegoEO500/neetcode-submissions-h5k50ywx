class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        A1 = list(s)
        A2 = list(t)

        A1.sort()
        A2.sort()

        if A1 == A2: 
            return True

        else:
            return False
        
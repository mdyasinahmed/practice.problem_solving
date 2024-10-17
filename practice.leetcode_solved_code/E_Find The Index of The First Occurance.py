class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        one = len(haystack)
        two = len(needle)

        for i in range(one-two+1):
            if haystack[i:i + two] == needle:
                return i

        return -1
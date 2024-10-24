class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])

        for word in words:
            temp = Counter(word)
            for char in count:
                count[char] = min(count[char], temp[char])

        return list(count.elements())
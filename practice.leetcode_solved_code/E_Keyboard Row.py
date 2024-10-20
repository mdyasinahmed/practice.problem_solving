class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        rows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
        
        for word in words:
            lowerWord = set(word.lower())
            if any(lowerWord <= row for row in rows):
                res.append(word)

        
        return res
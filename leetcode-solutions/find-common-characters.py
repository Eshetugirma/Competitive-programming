class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        data = collections.Counter(words[0])
        print(data)
        for word in words:
            data2 = collections.Counter(word)
            
            for k in data.keys():
                data[k] = min(data[k], data2[k])
        return data.elements()
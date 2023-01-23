class Solution:
    def sortSentence(self, s: str) -> str:
        # ==>> convert given sting to list then declare my dictionry 
        lists = list(s.split(" "))
        dic = {}
        target = 0
        # ==>> iterate word in sentence to identfy their sorting integer
        for word in lists:
            temp =''
            # ==>> iterate each words to separate and hold both integer and character in them 
            for i in range(len(word)):
                if word[i].isdigit():
                    target = int(word[i])
                else:
                    temp += word[i]
            # ==>> put in dictionary every words as value and use integer as sorting key
            dic[target] = temp
        # ==>> sort dictionary by integer in them 
        sorted_dict = sorted(dic.items(), key = lambda x:x[0])
        ans = list((dict(sorted_dict)).values())
        # ==>>> this final answer after converted to list all sorted words
        return ' '.join(ans)
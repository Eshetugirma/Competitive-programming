class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedList = []
        len1,len2 = len(word1),len(word2)
        minLen = min(len1,len2)
        for i in range(minLen):
            mergedList.append(word1[i])
            mergedList.append(word2[i])
        if len1 > minLen:
            return "".join(mergedList)+word1[minLen:]

        elif len2 > minLen:
             return "".join(mergedList)+word2[minLen:]
        else:
            return "".join(mergedList)
       
        
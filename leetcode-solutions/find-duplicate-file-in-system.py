class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for path in paths:
            path = path.split(" ")
            folder = path[0]
            for s in path[1:]:
                s = s.split(".txt")
                name = s[0]
                content = s[1]
                dic[content].append((folder,name))
        ans = []
        for k,v in dic.items():
            if len(v)>1:
                temp = []
                for path,name in v:
                    temp.append(path+'/'+name+'.txt')
                ans.append(temp)
        return ans
                    
        
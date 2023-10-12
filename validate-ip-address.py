class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        colon = queryIP.count(":")
        dot = queryIP.count(".")
        if (dot and colon) or (not colon and not dot):
            return "Neither"
        elif dot and "00" == queryIP[:2] or ".00" in queryIP:
            return "Neither"
        elif "::" in queryIP or ".." in queryIP:
            return "Neither"
        elif dot != 3 and colon != 7  or queryIP[-1] == "." or queryIP[-1] == ":":
            return "Neither"
        elif queryIP[0] == "." or queryIP[0] == ":":
            return "Neither"
        
        if dot == 3 and len(queryIP) < 20:
            left = 0
            index = []
            if queryIP[0] == "0" and queryIP[1] != ".":
                return "Neither"
            for right in range(1,len(queryIP)-1):
                if queryIP[right] == ".":
                    index.append(right)
                    if (right-left-1) > 4: 
                        return "Neither"
                    left = right
                
                elif queryIP[right] == "0" and right-1 == left:
                    if queryIP[right+1] != '0' and queryIP[right+1] != '.':
                        return "Neither"
                elif not queryIP[right].isdigit():
                    return "Neither"
            if int(queryIP[:index[0]]) > 255 or int(queryIP[index[0]+1:index[1]]) > 255 or int(queryIP[index[1]+1:index[2]]) > 255 or int(queryIP[index[2]+1:]) > 255:
                return "Neither"
            
                
            return "IPv4"
        # return 
        # print(queryIP[0])
        # print()
        elif colon == 7 and len(queryIP) < 40:
            left = 0
            # index = []
            # print(left)

            for right in range(1,len(queryIP)-1):

                if queryIP[right] == ":":
                    # index.append(right)
                    if (right-left-1) > 4: 
                        return "Neither"
                    left = right
                elif not queryIP[right].isdigit():
                    if queryIP[right].lower() > 'f' or queryIP[0].lower() > 'f':
                        return "Neither"

            # print(len(queryIP),left)
            if len(queryIP) - left - 1 > 4:
                return "Neither"
            return "IPv6"
        return "Neither"
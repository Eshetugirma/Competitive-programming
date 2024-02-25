class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        hour = 0
        finish = ((int(logoutTime[:2])*60 + int(logoutTime[3:])))
        start = (int(loginTime[3:]) + int(loginTime[:2])*60)
        if finish < start:
            hour += 24*60
        finish -= finish%15
        if start%15:
            start = start - start%15 + 15
        hour += (finish - start)
        print(finish,start)

        return hour//15 if hour > 0 else 0
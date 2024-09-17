def removecolons(s):
    if(len(s)==4):
        s=s[:1]+s[2:]
    if(len(s)==5):
        s=s[:2]+s[3:]
    return int(s)
def diff(s1,s2):
    time1=removecolons(s1)
    time2=removecolons(s2)
    hourdiff=time2//100-time1//100-1
    minDiff=time2%100+(60-time1%100)
    if(minDiff>=60):
        hourdiff+=1
        minDiff=minDiff-60
        res=str(hourdiff)+':'+str(minDiff)
    return res
s1=input("enter the time in this format(HH:MM):")
s2=input("enter the time in this format(HH:MM):")
print(diff(s1,s2))

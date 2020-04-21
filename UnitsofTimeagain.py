time = int(input())
days = time // 86400
time1 = time - (days * 86400)
hours = time1 // 3600
if hours < 10:
    c = 0
else:
    c = ""
time2 = time1 - (hours * 3600)
minutes = time2 // 60
if minutes < 10:
    b = 0
else:
    b = ""
seconds = time2 - (minutes * 60)
if seconds < 10:
    a = 0
else:
    a = ""
print (days, ":", c, hours,":",b, minutes, ":", a , seconds)
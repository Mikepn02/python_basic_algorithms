try:
    fhand=open('mboxes.txt')
except:
    print("file not found") 

mailCount = {}

for lines in fhand:
    line = lines.rstrip()
    if line.startswith('From '):
     stripline = line.split()
    #  print(stripline[2])
     day = stripline[2]
     mailCount[day] = mailCount.get(day,0) + 1

    #  if day in mailCount:
    #     mailCount[day] +=  1
    #  else:
    #     mailCount[day] = 1

print(mailCount)   
    
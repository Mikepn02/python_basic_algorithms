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
     domain = stripline[1]
     letter = '@'
     index = domain.index(letter)
     sliced = domain[index:]
     mailCount[sliced] = mailCount.get(sliced,0) + 1
    #  mailCount[day] = mailCount.get(day,0) + 1

    #  if day in mailCount:
    #     mailCount[day] +=  1
    #  else:
    #     mailCount[day] = 1

print(mailCount)   
    
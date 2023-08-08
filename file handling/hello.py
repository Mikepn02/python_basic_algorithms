greet=open('greet.text')
count=0
for lines in greet:
    line = lines.rstrip()
    if line.startswith('where'):
     print(line)
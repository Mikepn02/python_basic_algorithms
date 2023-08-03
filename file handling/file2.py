fname = input('enter the file name: ')

count=0

try:
    fhand= open(fname)

except:
    print("The file with that name not found ❌")
    exit()
for lines in fhand:
    line = lines.rstrip()
    if line.startswith('Received'):
        print(line)
    

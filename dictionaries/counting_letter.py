word= "anna has two bananas"
count= {}
for letter in word:
    if letter in count:
        count[letter] = count[letter] + 1
    else:
        count[letter] = 1
print (count.get('z','not letter found!!!'))
counts = {'Gloria' : 84,'jackson': 100,'shema':98}
lst = list(counts.keys())
print(lst)
lst.sort()
for key in lst:
    print(counts,counts[key])
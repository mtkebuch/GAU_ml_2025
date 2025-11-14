l = [4, 9.7, "gau"]
print(l)
print(l[1])

print("======")

t = (4, 9.7, "gau")
print(t)
print(t[1])
#t[1] = 87 ar sheidzleba

s = {4,5,6,78,32,1}
print(s)
s.add(34)
print(s)
#print(s[1]) ar sheidzleba

#aucilebelia carieli dictionary ganvsazgvrot da mere chavamatot elemetebi:
d = {}
d['uni'] = "Gau"
d['name'] = "Mari"
print(d)

list = [2,1,4,5,3]
print(sum(list))
print(min(list))
print(max(list))
#avg
avg = sum(list) / len(list)
print(avg)

list.append(102)
print(list)

list.insert(2,205)
print(list)

del list[3]
print(list)


import random
import statistics

#2
l = [2,35,1]
print(max(l))

#6

for _ in range(10):
    print(random.randint(1,89))

#8
def average(a,b):
    return (a+b)/20
average(4,2)
average(6,7)
average(2,1)

#11
def is_odd(n):
    return n%2 !=0

print(is_odd(5))
print(is_odd(40))
print(is_odd(7))

#15
nums = [2,1,4,5,3]
print(sum(nums))
print(min(nums))
print(max(nums))

average=sum(nums)/len(nums)
print(average)

nums.append(102)
print(nums)

nums.insert(2,205)
print(nums)

nums.pop(3)
print(nums)

nums.sort()
print(nums)

#19 list comprehension
n = [1,2,4,56,3,2,21,3]
new_list=[ x for x in n if x % 2 == 0]
print(new_list)

#21
sia = []
for _ in range(10):
    sia.append(random.randint(25,110))

print(sia)
print(min(sia))

#24
shuffledSia=[1,2,3,4,5,6,7,8,9,10]
random.shuffle(shuffledSia)
print(shuffledSia)

#27
sia_1=[1, 5, 23, 5, 12, 2, 5, 1, 18, 5]

most_common = max(sia_1,key=sia_1.count)
count=sia_1.count(most_common)

print("yvelaze xshirad gameorebuli ricxvi",most_common)
print("ramdenjer ganmeorda:",count)

#29
s = 'python php pascal javascript java c++'
words = s.split()
print(words)
longest_word=max(words,key=len)
print("yvelaze didi sityva:",longest_word)

#30
sia3 = [1,2,3,5,3,2,3,9,4,7]

avg = statistics.mean(sia3)
print("sashualo",avg)
med = statistics.median(sia3)
print("mediana",med)

try:
    mod=statistics.mode(sia3)
    print("moda",mod)

except statistics.StatisticsError:
    print("moda ar arsebobs")







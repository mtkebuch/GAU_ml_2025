import random
import statistics

#1
a=2
b=4
c=3
print(max(a,b,c))

#2
nums=[random.randint(1,100) for _ in range(10)]
print(nums)

#3
numbs=[1,2,3,4,5]
print(sum(numbs))
print(min(numbs))
print(max(numbs))
print(statistics.mean(numbs))
numbs.append(102)
print(numbs)
numbs.insert(2,205)
print(numbs)

numbs.sort()
print(numbs)

#
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

#
sia=[1,2,3,4,5]
random.shuffle(sia)
print(sia)



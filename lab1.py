#1
num = input("sheiyvanet ricxvi:")
num = int(num)
binary = bin(num)
print("orobiti",binary[2:])

#2
num1=int(input("sheiyvanet pirveli ricxvi:"))
num2=int(input("sheiyvanet meore ricxvi:"))
num3=int(input("sheiyvanet mesame ricxvi:"))

sashualo=(num1+num2+num3)/3
print("ricxvebis sashualo:",sashualo)

#3
num=int(input("sheitanet ricxvi:"))
if(num % 10 == 0):
    print("ricxvi bolovdeba nulit")
else:
    print("ricxvi ar bolovdeba nulit")

#4
year=int(input("sheiyvanet weli:"))
if(year % 4==0 and year % 100 !=0) or (year % 400==0):
  print(year,"aris nakiani weliwadi")
else:
  print(year,"ar aris nakiani weliwadi")

#5
for i in range(20,126):
 if i % 5 == 0:
  print(i)

#6
sum=0

for i in range(10):
 num=int(input("sheiyvanet ricxvi:"))
 sum+=num

average=sum/10
print("ricxvebis sashualo:",average)

#7
a=int(input("sheiyvanet pirveli ricxvi:"))
b=int(input("sheiyvanet meore ricxvi:"))

if a<=0 or b<=0:
  print("ricxvebi unda iyos dadebiti")
else:
      while b!=0:
         a, b = b, a % b
      print("udidesi gamyofi:",a)
#8
n=int(input("sheiyvanet ricxvi:"))

for i in range(1,n+1):
    if n % i == 0:
       print(i)
#9
for num in range(2, 1001):
    prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)
#10
n=input("sheiyvanet ricxvi:")
n=int(n)
count=0
while n!=0:
  n=n//10
  count+=1
  print("cifrebis raodenoba",count)

#11
n=input("sheikvanet ricxvi:")
if n==n[::-1]:
  print("palindromia")
else:
  print("ar aris palindromi")

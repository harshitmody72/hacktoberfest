# palindrom

a = input("Enter a Number :")
c = len(a)
sum = 0
j= 1
for i in a :
    i = int(i)
    sum += i * (10**(c - j))
    j +=1
print(sum)
a = int(a)
if sum == a :
    print("Yes")
else:
    print("No")

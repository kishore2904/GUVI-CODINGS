num,a,b=input().split()
num=int(num)
a=int(a)
b=int(b)
sum=0
for i in range(num):
    sum=sum+a
    a=a+b
print(sum)

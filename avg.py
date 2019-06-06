a=int(input(""))
num=list(input().split())
sum=0
for i in range(1,a):
    sum=sum+int(num[i])
d=len(num)
av=sum//d
print(av)

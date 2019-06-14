n1=int(input())
count=0
a=[]
for i in range(n1):
    a.append(input())
for i in range(n1):
    if sorted(a[i])==sorted('kabali'):
        count=count+1
print(count)   

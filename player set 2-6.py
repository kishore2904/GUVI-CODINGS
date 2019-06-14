dumy=int(input())
n=[int(x) for x in input().split()]
f={}
for i  in n:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
p=min(f,key=f.get)
print(p)

v1=input()
v1=list(v1)
v1[::2],v1[1::2]=v1[1::2],v1[::2]
print(*v1,sep="")

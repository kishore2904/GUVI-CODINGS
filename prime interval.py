a,b=input("").split()
a=int(a)+1
b=int(b)
for i in range(a,b):
    c=0
    for y in range(1,b):
       if(i%y==0):
         c=c+1
    if(c==2):
       print(i,end=" ")

e1=input()
e1=e1.split(" ")
e1=list(map(int,e1))
f=e1[0]
g=e1[1]
if(f>g):
    smaller=g
else:
    smaller=f
for i in range(1,smaller+1):
         if((f%i==0) and (g%i==0)):
                h=i
print(h)

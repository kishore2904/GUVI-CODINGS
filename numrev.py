a=int(input())
c=0
while(a>0):
    rev=a%10
    c=(c*10)+rev
    a=a//10
print(c)   

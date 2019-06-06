num1,num2=input().split()
num1=int(num1)+1
num2=int(num2)
for i in range (num1,num2):
    c=i%2
    if(c!=0):
       print(i,end="")

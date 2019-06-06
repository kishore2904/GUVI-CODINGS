num1,num2=input("").split()
num1=int(num1)
num2=int(num2)
for i in range(num1,num2):
     s=0
     a=i
     while(i!=0):
          rem=i%10
          s=s+rem*rem*rem
          i//=10
     if(a==s):
        print(a,end=" ")

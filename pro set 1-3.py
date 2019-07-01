num,num1=input().split()
v=abs(len(num)-len(num1))
for i in range(len(num)):
  if len(num1)==1 and num1[i] in num:
   break
  if num[i]!=num1[i]:
   v+=1
print(v)

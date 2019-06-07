R=input()
m=r=0;
for i in R:
    if i.isalpha():
        r+=1 
    elif i.isnumeric():
        m+=1 
if(m>=1 and r>=1):
    print("Yes")
else:
    print("No")

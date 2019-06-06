n=int(input("")
tem=n
rem=tem//2
cou=0
for i in range(1,rem):
    if(tem%i==0):
    cou=cou+1
if cou>1:
    print("no")
else:
    print("yes")

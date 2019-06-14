t1=list(map(int,input().split()))
for i in range(1,(t1[0]*t1[1])+1):
    if(i%t1[0]==0 and i%t1[1]==0):
        print(i)
        break

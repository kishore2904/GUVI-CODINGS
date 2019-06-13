ss,s1=map(str,input().split())
cnt=0
for i in range(len(ss)):
    if ss[i]!=s1[i]:
        cnt+=1 
if cnt==1:
    print("yes")
else:
    print('no')

k1,s=map(str,input().split())
l=0
if len(k1)>len(s):
  k1,s=s,k1
i=0
while i<len(k1):
  l+=(ord(s[i])-ord(k1[i]))
  i+=1
for i in range(i,len(s)):
  l+=ord(s[i])-ord('a')+1
print(l)

ig=int(input())
l=[int(x) for x in input().split()[:ig]]
for u in l:
  if(l.count(u)==1):
    print(u,end=" ")

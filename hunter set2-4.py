ee=int(input())
g=input()  
h=[]
g=list(g)  
for j in g:
      if(j=='A' or j=='E' or j=='I' or j=='O' or j=='U' or j=='a' or j=='e' or j=='i' or j=='o' or j=='u'):
          g.remove(j)
          h.append(j) 
i=g[ ::-1 ]
print(*i,sep="") 

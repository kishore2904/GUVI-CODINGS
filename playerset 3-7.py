    
sa=list(map(str,input()))
for i in range(len(sa)):
  if sa[i].islower()==True:
        sa[i]=s[i].capitalize()
  else:
        sa[i]=sa[i].lower()
for i in range(len(sa)): print(sa[i],end="")

x=int(input(""))
re=x
rev=0
while(x>0):
   div=x%10
   rev=rev*10+div
   x=x//10
if(re==rev):
   print("yes")
else:
   print("no")

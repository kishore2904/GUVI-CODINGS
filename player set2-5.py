string = input()
dic1 = {}
for i in string:
    if i in dic1:
        dic1[i]+=1
    else:
        dic1[i]=1
maxi = max(dic1,key=dic1.get)
print(maxi)

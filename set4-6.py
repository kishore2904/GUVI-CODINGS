string=input()
cout=0
for i in range(len(string)):
    if(string[i].isalnum()):
        cout+=1
print(len(string)-cout)

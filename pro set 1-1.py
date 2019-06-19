def common_prefix():
    list1=[]
    for i in zip(*b):
        if (i.count(i[0])==len(i)): 
            list1.append(i[0])
        else:
            break
    print(''.join(list1))
a=int(input())
b=[]
for i in range(0,a):  
    u=input()
    b.append(u)
common_prefix()

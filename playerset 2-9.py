n1=int(input())
i=1
while(i<=n1):
    c=0
    if(n1%i==0):
        j=1
        while(j<=i):
            if(i%j==0):
                c=c+1
            j=j+1
        if(c==2):
            print(i,end=' ')
    i=i+1

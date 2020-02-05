counter=2
n=10001
eq=False
for i in range(3,1000000,2):
    k=1
    if eq==True:
        break
    while k<i:
        k+=2
        if i%k==0:
            break
        if k+2==i:
            counter+=1
        if counter==n:
            print(i)
            eq=True
            break
    if eq==True:
        i=1000000-2
        break
    

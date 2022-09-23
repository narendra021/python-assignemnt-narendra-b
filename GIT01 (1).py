t=int(input())
for k in range(t):
    n, m=map(int, input().split())
    r=0
    g=0 
    for i in range(n):
        a=input()
        if i%2==0:
            for j in range(m):
                if j%2==0 and a[j]=="R":
                    g+=5 
                elif j%2!=0 and a[j]=="G":
                    g+=3 
                if j%2==0 and a[j]=="G":
                    r+=3 
                elif j%2!=0 and a[j]=="R":
                    r+=5 
        else:
            for j in range(m):
                if j%2==0 and a[j]=="G":
                    g+=3 
                elif j%2!=0 and a[j]=="R":
                    g+=5 
                if j%2==0 and a[j]=="R":
                    r+=5 
                elif j%2!=0 and a[j]=="G":
                    r+=3 
    if g>r:
        print(r)
    else:
        print(g)
                
                    
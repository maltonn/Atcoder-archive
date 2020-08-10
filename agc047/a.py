def main():#TLE
    import sys
    N=int(input())
    L=[]
    for i in range(N):
        s=input()
        if '.' not in s:
            n=int(s)
            m=0
        else:
            n=int(s.replace('.',''))
            m=len(s)-s.find('.')-1
            
        
        n2=n
        n5=n

        c2=0
        while n2%2==0:
            n2//=2
            c2+=1
        
        c5=0
        while n5%5==0:
            n5//=2
            c5+=1
        
        L.append((c2,c5,m))
    count=0
    for i in range(N):
        for j in range(i+1,N):
            tup1=L[i]
            tup2=L[j]
            if min(tup1[0]+tup2[0],tup1[1]+tup2[1])>=tup1[2]+tup2[2]:
                count+=1

    print(count)
main()

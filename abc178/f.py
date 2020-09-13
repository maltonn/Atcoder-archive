def main():#WA(only 1)
    import sys
    from collections import Counter
    N=int(sys.stdin.readline())
    A=list(map(int,sys.stdin.readline().split()))
    B=list(map(int,sys.stdin.readline().split()))
    
    AC=Counter(A)
    BC=Counter(B)

    for a in AC:
        if a in BC:
            if AC[a]+BC[a]>N:
                print('No')
                return

    L=[0]*N
    BS=set(B)
    ABC=Counter(A+B)
    ABT=sorted(ABC.items(),key=lambda x:-x[1])
    K=[]
    for n,_ in ABT:
        for _ in range(AC[n]):
            K.append(n)

    K2=[]
    for n,_ in ABT:
        for _ in range(BC[n]):
            K2.append(n)

    not_yet=[]
    for i in range(AC[ABT[0][0]]):
        not_yet.append(i)
    
    idx=AC[ABT[0][0]]
    if idx==N:
        print('Yes')
        print(' '.join(map(str,B)))
        return
    for j,n in enumerate(K2):
        flag=False
        while K[idx]==n:
            not_yet.append(idx)
            idx+=1
            if idx==N:
                start=j+1
                flag=True
                break

        if flag:
            break

        L[idx]=n
        idx+=1
        if idx==N:
            start=j+1
            break
    
    idx=0
    midx=1
    for n in K2[start:]:
        if K[not_yet[idx]]==n:
            L[not_yet[-midx]]=n
            midx+=1
        else:
            L[not_yet[idx]]=n
            idx+=1
    
    tmp=sorted([(x,y) for x,y in zip(K,L)],key=lambda x:x[0])
    out=[y for x,y in tmp]
        
    print('Yes')
    print(' '.join(map(str,out)))
main()
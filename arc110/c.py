def main():
    import sys
    N=int(sys.stdin.readline())
    P=list(map(int,sys.stdin.readline().split()))
    output=[]
    L=[0]*(N+1)#L[0]は常に0
    for i in range(N):
        L[P[i]]=i


    now=1
    prev=0
    while True:
        if now>=len(L):
            break
        pos=L[now]
        for i in range(pos,prev,-1):
            output.append(i) #L[i-1] <-> L[i] (1-idx)  
            L[P[i]]-=1
            L[P[i-1]]+=1
            P[i],P[i-1]=P[i-1],P[i]

        # print('O',output)
        # print('L',L)
        # print('P',P)
        # print('now',now)
        # print('---')
        for j,a in enumerate(range(prev,pos)):
            if L[now+j]!=a:
                print(-1)
                return
    
        prev=pos
        now=pos+1
        while L[now]==now-1:
            now+=1
            if now>=len(L):
                break
    
    if len(output)!=N-1:
        print(-1)
        return

    for res in output:
        print(res)
    


if __name__=='__main__':
    main()
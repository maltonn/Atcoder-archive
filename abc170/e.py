def main():
    import sys
    import heapq
    from collections import defaultdict
    N,Q=list(map(int,sys.stdin.readline().split()))
    L=[() for _ in range(N)]
    L2=[[] for _ in range(2*10**5+2)]
    L4=[{} for _ in range(2*10**5+2)]
    
    for l in L2:
        heapq.heapify(l)

    for i in range(N):
        A,B=list(map(int,sys.stdin.readline().split()))
        L[i]=[A,B]
        heapq.heappush(L2[B],-A)
        if A in L4[B].keys():
            L4[B][A]+=1
        else:
            L4[B][A]=1


    maxes=[-hp[0] if len(hp) else 10**9+1 for hp in L2]
    mn=min(maxes)

    for i in range(Q):
        C,D=list(map(int,sys.stdin.readline().split()))
        
        C-=1

        a=L[C][0]
        b=L[C][1]
        
        L4[b][a]-=1

        while len(L2[b]) and L4[b][-L2[b][0]]==0:
            heapq.heappop(L2[b])

        if mn==maxes[b]:
            flag=True
        else:
            flag=False

        if len(L2[b]):
            maxes[b]=-L2[b][0]
            if flag:
                mn=min(maxes)
        else:
            maxes[b]=10**9+1

        if a in L4[D].keys():
            L4[D][a]+=1
        else:
            L4[D][a]=1


        heapq.heappush(L2[D],-a)
        if mn==maxes[D]:
            flag=True
        else:
            flag=False
        maxes[D]=-L2[D][0]
        
        if flag:
            mn=min(maxes)



        L[C][1]=D
        print(mn)
        print(L2[2019:2022])

main()
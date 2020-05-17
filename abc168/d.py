def main():
    import sys
    from collections import defaultdict,deque
    sys.setrecursionlimit(10**5+2)

    N,M=list(map(int,sys.stdin.readline().split()))
    dic=defaultdict(list)
    for i in range(M):
        A,B=list(map(int,sys.stdin.readline().split()))
        dic[A].append(B)
        dic[B].append(A)
    
    L=[-1]*(N+1)
    R=[-1]*(N+1)


    d = deque()
    d.append((1,1))
    while len(d):
        now,count=d.popleft()
        for goto in dic[now]:
            if L[goto]==-1 or count<L[goto]:
                L[goto]=count
                R[goto]=now
                d.append((goto,count+1))

    if any(x+1 for x in R[2:]):
        print('Yes')
        for x in R[2:]:
            print(x)
    else:
        print('No')
    


main()
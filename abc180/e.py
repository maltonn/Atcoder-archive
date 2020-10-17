def main():
    import sys
    
    N=int(sys.stdin.readline())
    L=[]
    for i in range(N):
        X,Y,Z=list(map(int,sys.stdin.readline().split()))
        L.append((X,Y,Z))

    lst=[[0]*N for _ in range(N)]
    for i,(a,b,c) in enumerate(L):
        for j,(p,q,r) in enumerate(L):
            if i==j:
                continue
            lst[i][j]=abs(p-a)+abs(q-b)+max(0,r-c)
            lst[j][i]=abs(p-a)+abs(q-b)+max(0,c-r)

    def Path2Bin(path):
        return sum([x*2**i for i,x in enumerate(path)])#逆だけど気にしない

    memo=[[-1]*(2**N) for _ in range(N)]
    
    def dfs(path,now,dist):
        if memo[now][Path2Bin(path)]+1:
            return memo[now][Path2Bin(path)]
        path[now]=1
        if all(path):
            return dist+lst[now][0]
        out=10**9
        for j in range(N):
            if path[j]:
                continue
            dist+=lst[now][j]
            res=dfs(path.copy(),j,dist)
            out=min(res,out)
        memo[now][Path2Bin(path)]=out
        return out

    print(dfs([0]*N,0,0))

main()
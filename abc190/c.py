def main():
    import sys
    N,M=list(map(int,sys.stdin.readline().split()))
    L=[]
    for i in range(M):
        A,B=list(map(int,sys.stdin.readline().split()))
        L.append((A,B))
    K=int(sys.stdin.readline())

    L2=[]
    for i in range(K):
        C,D=list(map(int,sys.stdin.readline().split()))
        L2.append((C,D))

    def dfs(i,tup):
        if i==K:
            count=0
            L3=[0]*N
            for t in tup:
                L3[t-1]=1
            for a,b in L:
                if L3[a-1] and L3[b-1]:
                    count+=1

            return count
        
        c1=dfs(i+1,tup+(L2[i][0],))
        c2=dfs(i+1,tup+(L2[i][1],))
        
        return c1 if c1>c2 else c2

    print(dfs(0,tuple()))
    

if __name__ == "__main__":
    main()
def main():
    import sys
    N=int(sys.stdin.readline())
    L=[-1]*N
    for i in range(N):
        s=sys.stdin.readline().strip()
        if s=='AND':
            L[i]=0
        else:
            L[i]=1
    
    L.reverse()
    
    def dfs(i):
        if i==N:
            return 1
        if L[i]:#OR
            res1=2**(N-i)
            res2=dfs(i+1)
            return res1+res2
        else:#and
            res2=dfs(i+1)
            return res2

    print(dfs(0))

if __name__ == "__main__":
    main()
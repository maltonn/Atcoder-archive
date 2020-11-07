def main():
    import sys
    N,S=list(map(int,sys.stdin.readline().split()))
    def dfs(a,idx,tup):
        if a==S and idx==N:
            print(' '.join([str(x) for x in tup]))
            return
        for i in range(tup[-1] if tup else 1,51):
            if a+i<=S:
                if tup:
                    dfs(a+i,idx+1,tup+(i,))
                else:
                    dfs(a+i,idx+1,(i,))
            else:
                break
    
    dfs(0,0,None)

main()
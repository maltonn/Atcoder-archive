def main():#WA
    import sys
    A,B,C,D=list(map(int,sys.stdin.readline().split()))
    tate_diff=C-A
    yoko_diff=D-B
    memo=[[-1]*(yoko_diff+1) for _ in range(tate_diff+1)]
    mod=998244353
    sys.setrecursionlimit(4000)

    def dfs(tate,yoko,total,istate,prev_total):
        #print(tate,yoko,total)
        if memo[tate][yoko]!=-1:
            #print('k',memo[tate][yoko],total)
            if istate:
                return (memo[tate][yoko]*(A+tate-1)*prev_total)%mod
            else:
                return (memo[tate][yoko]*(B+yoko-1)*prev_total)%mod
        if tate_diff==tate:
            res1=0
        else:
            res1=dfs(tate+1,yoko,total*(B+yoko)%mod,True,total)
        if yoko_diff==yoko:
            res2=0
        else:
            res2=dfs(tate,yoko+1,total*(A+tate)%mod,False,total)

        if res1+res2==0:
            res1=total

        memo[tate][yoko]=((res1+res2)//total)
        return (res1+res2)%mod

    print(dfs(0,0,1,None,0))


main()
def main():#under constructing
    import sys
    H,W=list(map(int,sys.stdin.readline().split()))
    Ch,Cw=list(map(int,sys.stdin.readline().split()))
    Dh,Dw=list(map(int,sys.stdin.readline().split()))
    Meiz=[[0]*W for _ in range(H)]
    memo=[[10**6]*W for _ in range(H)]
    

    for i in range(H):
        S=sys.stdin.readline().strip()
        for j,s in enumerate(S):
            Meiz[i][j]=0 if s=='#' else 1


    def dfs(y,x,count,iswall):
        pass

    start=Meiz[Dh][Dw]

main()
def main():#not complete
    import sys
    from collections import defaultdict
    from collections import defaultdict
    alps=set([chr(i) for i in range(97, 97+26)])
    dic1=defaultdict(list)
    dic2={}

    H,W=list(map(int,sys.stdin.readline().split()))
    M=[[0]*W for _ in range(H)]
    MD=[[10**6]*W for _ in range(H)]
    
    start=(-1,-1)
    goal=(-1,-1)

    for i in range(H):
        for j,s in enumerate(sys.stdin.readline().strip()):
            if s=='.':
                M[i,j]=1
            elif s=='#':
                M[i,j]=0
            elif s=='S':
                start=(i,j)
            elif s=='G':
                goal=(i,j)
            else:
                dic1[s].append((i,j))
    
    for key in dic1:
        dic2[dic1[key][0]]=dic1[key][1]
        dic2[dic1[key][1]]=dic1[key][2]

    def dfs(y,x,dist):
        
        MD[y][x]=min(dist)

        for tate in [-1,0,1]:
            for yoko in [-1,0,1]:
                if (tate or yoko) and not (tate and yoko):
                    ny=y+tate
                    nx=x+yoko
                    if 0<=ny<H and 0<=nx<W and M[ny][nx]:
                        dfs(ny,nx,dist+1)
                    

if __name__ == "__main__":
    main()
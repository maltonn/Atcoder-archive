def main():
    import sys
    N=int(sys.stdin.readline())
    L=[]
    OP=[]
    OPs=[]
    for i in range(N):
        x,y=list(map(int,sys.stdin.readline().split()))
        L.append((x,y))
    M=int(sys.stdin.readline())
    for i in range(M):
        op=tuple(map(int,sys.stdin.readline().split()))
        OP.append(op)

    now=[[1,0],[1,0],1]
    for op in OP:
        com=op[0]
        if com==1:
            now[0],now[1]=now[1],now[0]
            now[1][0]*=-1
            now[1][1]*=-1
            now[2]*=-1
        elif com==2:
            now[0],now[1]=now[1],now[0]
            now[0][0]*=-1
            now[0][1]*=-1
            now[2]*=-1
        elif com==3:
            now[0][0]*=-1
            now[0][1]=op[1]*2-now[0][1]
        elif com==4:
            now[1][0]*=-1
            now[1][1]=op[1]*2-now[1][1]
        

        OPs.append((tuple(now[0]),tuple(now[1]),now[2]))
    #print(OPs)

    Q=int(sys.stdin.readline())
    for i in range(Q):
        a,b=list(map(int,sys.stdin.readline().split()))
        x,y=L[b-1]
        if a!=0:
            #print('--',OPs[a-1],x,y)
            (pnx,dx),(pny,dy),flip=OPs[a-1]
            if flip==1:
                x=x*pnx+dx
                y=y*pny+dy
            else:
                x_memo=x
                x=y*pnx+dx
                y=x_memo*pny+dy
                
        print('{} {}'.format(x,y))
            

if __name__ == "__main__":
    main()
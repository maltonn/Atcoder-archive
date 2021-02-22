def main():
    import sys
    N,X=list(map(int,sys.stdin.readline().split()))
    A=list(map(int,sys.stdin.readline().split()))
    A.sort()

    LL=[[0]*N for _ in range(N)]
    LD=[{} for _ in range(N)]
    for i in range(N):
        for j in range(N):
            t=A[j]%(i+1)
            LL[i][j]=t
            if t in LD[i]:
                LD[i][t]+=1
            else:
                LD[i][t]=1
    
    res=10**19
    for i in range(N):#i+1種類の素材を使う
        md=i+1
        target=X%md
        #LL[i]からmd個選んで合計Sをmdで割った余りがtarget
        


if __name__=='__main__':
    main()
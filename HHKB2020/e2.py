def main():#TLE
    import sys
    #import time
    #start=time.time()

    mod=1000000007
    
    H,W=list(map(int,sys.stdin.readline().split()))
    room=[[0]*W for _ in range(H)]
    memo_tate=[[0]*W for _ in range(H)]
    memo_yoko=[[0]*W for _ in range(H)]

    K=0
    for i in range(H):
        for j,s in enumerate(sys.stdin.readline().strip()):
            if s=='.':
                room[i][j]=1
                K+=1
    tmp=0
    for i in range(H):
        for j in range(W):
            if not room[i][j]:
                continue
            
            if memo_yoko[i][j]:
                print('pass:',memo_yoko)
                t=memo_yoko[i][j]

            else:
                print(memo_yoko,i,j)
                k=0
                while True:
                    tmp+=1
                    k+=1
                    if j+k==W or not room[i][j+k]:
                        break
                k2=0
                while True:
                    k2+=1
                    if j-k2==-1 or not room[i][j-k2]:
                        break           
                t=k+k2-1
                for l in range(j-k2+1,j+k):
                    memo_yoko[i][l]=t

            if memo_tate[i][j]:
                t=memo_tate[i][j]
            else:
                k=0
                while True:
                    k+=1
                    if i+k==H or not room[i+k][j]:
                        break
                k2=0
                while True:
                    k2+=1
                    if i-k2==-1 or not room[i-k2][j]:
                        break
                t=k+k2-1
                for l in range(i-k2+1,i+k):
                    memo_tate[l][j]=t

    res=0
    #print(time.time()-start)
    for i in range(H):
        for j in range(W):
            if not room[i][j]:
                continue
            t=int(memo_tate[i][j]+memo_yoko[i][j]-1)#np.int32 -> int
            res+=pow(2,K,mod)-pow(2,K-t,mod)
            res%=mod

    #print(time.time()-start)

    print(tmp)
    print(res)


main()
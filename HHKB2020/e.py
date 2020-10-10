def main():#TLE
    import sys
    mod=1000000007
    import numpy as np
    H,W=list(map(int,sys.stdin.readline().split()))
    room=np.zeros((H,W)).astype('int32')
    memo_tate=np.zeros((H,W)).astype('int32')
    memo_yoko=np.zeros((H,W)).astype('int32')

    for i in range(H):
        for j,s in enumerate(sys.stdin.readline().strip()):
            if s=='.':
                room[i,j]=1
    K=np.count_nonzero(room)



    for i in range(H):
        for j in range(W):
            if not room[i,j]:
                continue
            
            if memo_yoko[i,j]:
                t=memo_yoko[i,j]
            else:
                k=0
                while True:
                    k+=1
                    if j+k==W or not room[i,j+k]:
                        break
                k2=0
                while True:
                    k2+=1
                    if j-k2==-1 or not room[i,j-k2]:
                        break           
                t=k+k2-1
                memo_yoko[i,j-k2+1:j+k]=t

            if memo_tate[i,j]:
                t=memo_tate[i,j]
            else:
                k=0
                while True:
                    k+=1
                    if i+k==H or not room[i+k,j]:
                        break
                k2=0
                while True:
                    k2+=1
                    if i-k2==-1 or not room[i-k2,j]:
                        break
                t=k+k2-1
                memo_tate[i-k2+1:i+k,j]=t

    res=0
    for i in range(H):
        for j in range(W):
            if not room[i,j]:
                continue
            t=int(memo_tate[i,j]+memo_yoko[i,j]-1)#np.int32 -> int
            res+=pow(2,K,mod)-pow(2,K-t,mod)
            res%=mod

    print(res)


main()
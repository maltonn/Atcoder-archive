def main():
    import sys
    N,K=list(map(int,sys.stdin.readline().split()))
    A=list(map(int,sys.stdin.readline().split()))
    B=list(map(int,sys.stdin.readline().split()))

    if K==1:
        print(sum(B)+A[-1])
    
    if K==2:
        C=[A[i]-A[i-1]+b if i else a+b for i,(a,b) in enumerate(zip(A,B))]
    
        res=0
        for i in range(C):
            if res+C[i]>=A[-1]:
                C[i]-=A[-1]-res
                break
            res+=C[i]
            C[i]=0


if __name__=='__main__':
    main()
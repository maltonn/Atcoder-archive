def main():
    import sys
    N,K=list(map(int,sys.stdin.readline().split()))
    A=list(map(int,sys.stdin.readline().split()))

    Ap=[x for x in A if x>=0 ]
    Am=[abs(x) for x in A if x<0]

    if K==N:
        out=1
        for a in A:
            out*=a
            out%=10**9+7
        print(out)
        return


    if K%2==1 and len(Ap)==0:
        Am.sort()
        out=1
        for i in range(K):
            out*=Am[i]
            out%=10**9+7
        print((-out)%(10**9+7))
        return

    Ap.sort(reverse=True)
    Am.sort(reverse=True)
    
    ap_idx=0
    am_idx=0
    result=1

    for _ in range(0,K-1,2):
        if K%2==0 and ap_idx+1<len(Ap):
            pmax=Ap[ap_idx]*Ap[ap_idx+1]
        elif K%2==1 and ap_idx+2<len(Ap):
            pmax=Ap[ap_idx]*Ap[ap_idx+1]
        else:
            pmax=-1

        if am_idx+1<len(Am):
            mmax=Am[am_idx]*Am[am_idx+1]
        else:
            mmax=-1

        if pmax==-1 and mmax==-1:
            break

        if pmax>mmax:
            result*=pmax
            ap_idx+=2
        else:
            result*=mmax
            am_idx+=2

        result%=(10**9+7)
    
    if K%2==1:
        result*=Ap[ap_idx]

    print(result%(10**9+7))

main()
def main():
    import sys
    from math import gcd
    N,M=list(map(int,sys.stdin.readline().split()))
    A=list(map(int,sys.stdin.readline().split()))
    A.sort()
    if not A:
        print(1)
        return

    diff=[]
    if A[0]-1:
        diff.append(A[0]-1)
    
    for i in range(M-1):
        if A[i+1]-A[i]-1:
            diff.append(A[i+1]-A[i]-1)
    if N-A[-1]:
        diff.append(N-A[-1])
    
    if not diff:
        print(0)
        return

        
    md=min(diff)

    res=0
    for d in diff:
        res+=d//md
        if d%md:
            res+=1


    print(res)

if __name__ == "__main__":
    main()
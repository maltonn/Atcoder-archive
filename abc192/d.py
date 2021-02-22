def judge(X,M,n):
    s=0
    length=len(X)
    for i,x in enumerate(X):
        s+=x*n**(length-i-1)
    return s<=M


    
def main():
    import sys
    X=[int(x) for x in list(sys.stdin.readline().strip())]
    M=int(sys.stdin.readline())
    l=max(X)+1
    r=M+1
    m=max(X)+1
    while l<r:
        m=(l+r)//2
        res=judge(X,M,m)
        if res:
            l=m+1
        else:
            r=m-1
    if r==M+1:
        err
    for i in range(m-2,m+3):
        if not judge(X,M,i):
            print(i-1-max(X))
            break
    



if __name__ == "__main__":
    main()
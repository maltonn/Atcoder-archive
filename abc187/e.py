def main():
    import sys
    N=int(sys.stdin.readline())
    L=[]
    M=[0]*N
    for i in range(N):
        a,b=list(map(int,sys.stdin.readline().split()))
        L.append((a,b))

    Q=int(sys.stdin.readline())
    for q in Q:
        t,e,x=list(map(int,sys.stdin.readline().split()))
    

if __name__ == "__main__":
    main()
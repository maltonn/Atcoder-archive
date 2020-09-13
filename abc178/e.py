def main():
    import sys
    N=int(sys.stdin.readline())

    xpy=[]
    xmy=[]

    for i in range(N):
        x,y=list(map(int,sys.stdin.readline().split()))
        xpy.append(x+y)
        xmy.append(x-y)

    t1=max(xpy)-min(xpy)
    t2=max(xmy)-min(xmy)

    print(max(t1,t2))

main()
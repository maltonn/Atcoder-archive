def main():
    import sys
    N=int(sys.stdin.readline())
    if N==1:
        print(0)
        return
    m=10**9+7
    res=pow(10,N,m)-(2*pow(9,N,m)-pow(8,N,m))%m
    if res<0:
        print(res+m)
    else:
        print(res%m)

main()
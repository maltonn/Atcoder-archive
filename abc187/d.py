def main():
    import sys
    N=int(sys.stdin.readline())

    L=[]
    for i in range(N):
        L.append(tuple(map(int,sys.stdin.readline().split())))
    
    L.sort(key=lambda x:-(2*x[0]+x[1]))

    aoki=sum((a for a,b in L))
    res=0
    for a,b in L:
        res+=1
        aoki-=2*a+b
        if aoki<0:
            print(res)
            return   


if __name__ == "__main__":
    main()
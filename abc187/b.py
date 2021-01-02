def main():
    import sys
    N=int(sys.stdin.readline())

    L=[]
    for i in range(N):
        L.append(tuple(map(int,sys.stdin.readline().split())))

    res=0
    for i in range(N):
        for j in range(i+1,N):
            x1,y1=L[i]
            x2,y2=L[j]
            if x1!=x2:
                if abs(y2-y1)<=abs(x2-x1):
                    res+=1

    print(res)

if __name__ == "__main__":
    main()
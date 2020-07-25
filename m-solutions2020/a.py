def main():
    import sys
    X=int(sys.stdin.readline())
    L1=[400,600,800,1000,1200,1400,1600,1800,2000]
    L2=[8,7,6,5,4,3,2,1]
    for i in range(len(L1)):
        if L1[i]<=X<L1[i+1]:
            print(L2[i])
            break


main()
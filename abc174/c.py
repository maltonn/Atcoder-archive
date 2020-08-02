def main():
    import sys
    import time
    start=time.time()
    K=int(sys.stdin.readline())
    if K%2==0:
        print(-1)
        return

    L=[7%K]
    L2=[7%K]
    if L[0]==0:
        print(1)
        return

    idx=0
    while True:
        L2.append((L2[idx]*10)%K)
        L.append((L[idx]+L2[idx+1])%K)
        if L[-1]==0:
            print(len(L))
            return
        idx+=1

        if time.time()-start>=1.5:
            print(-1)
            return
main()
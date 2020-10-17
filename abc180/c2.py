def main():
    import sys
    N=int(sys.stdin.readline())
    out=[]
    if N==1:
        print(1)
        return
    for m in range(1,N):
        if N//m<m:
            break
        if N%m==0:
            out.append(m)
            out.append(N//m)
    

    for res in sorted(list(set(out))):
        print(res)
main()
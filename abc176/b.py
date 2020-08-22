def main():
    import sys
    S=sys.stdin.readline().strip()
    k=0
    for a in S:
        k+=int(a)

    if k%9==0:
        print('Yes')
    else:
        print('No')

main()
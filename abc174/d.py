def main():
    import sys
    N=int(sys.stdin.readline())
    C=[1 if c=='R' else 0 for c in sys.stdin.readline().strip()]
    R=C.count(1)
    print(C[:R].count(0))

main()
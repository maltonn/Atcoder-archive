def main():
    import sys
    S=sys.stdin.readline().strip()
    T=sys.stdin.readline().strip()
    if S=='Y':
        print(T.upper())
    else:
        print(T)

main()
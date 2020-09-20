def main():
    import sys
    S=sys.stdin.readline().strip()
    if S[-1]=='s':
        print(S+'es')
    else:
        print(S+'s')

main()
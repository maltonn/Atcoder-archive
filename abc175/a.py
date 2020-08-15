def main():
    import sys
    S=sys.stdin.readline().strip()
    if S=='RSR':
        print(1)
    else:
        print(S.count('R'))

main()
def main():
    import sys
    S=sys.stdin.readline()
    T=sys.stdin.readline()
    count=0
    for s,t in zip(S,T):
        count+=s!=t
    print(count)
main()
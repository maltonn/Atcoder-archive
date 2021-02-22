def main():
    import sys
    S=sys.stdin.readline().strip()
    s1=S[::2]
    s2=S[1::2]
    if s1==s1.lower() and s2==s2.upper():
        print('Yes')
    else:
        print('No')
        

if __name__ == "__main__":
    main()
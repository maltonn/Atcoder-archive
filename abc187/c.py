def main():
    import sys
    N=int(sys.stdin.readline())
    st=set()
    for i in range(N):
        sr=sys.stdin.readline().strip()
        if sr[0]=='!':
            if sr[1:] in st:
                print(sr[1:])
                return
        else:
            if '!'+sr in st:
                print(sr)
                return

        st.add(sr)
    
    print('satisfiable')

if __name__ == "__main__":
    main()
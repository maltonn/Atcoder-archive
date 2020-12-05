#e
def main():#RE,TLE
    import sys
    def D(s):
        if s[0]==s[1]:
            return False

        if 'A' not in s:
            return 'A'
        
        if 'B' not in s:
            return 'B'

        if 'C' not in s:
            return 'C'


    def dfs(S):
        #print(S)
        if len(S)==1:
            st.add(S)
            return
        
        st.add(S)
        for i in range(len(S)-1):
            d=D(S[i:i+2])
            if d:
                dfs(S[:i]+d+S[i+2:])
    N=int(sys.stdin.readline())
    S=sys.stdin.readline().strip()
    st=set()
    dfs(S)
    #print(sorted(st))
    print(len(st))

if __name__=='__main__':
    main()
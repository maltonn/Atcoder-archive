def main():
    for k in ['AA','AB','BA','BB']:
        ss=k[0]+'B'+k[1]+'A'
        dic={
            'AA':ss[0],
            'AB':ss[1],
            'BA':ss[2],
            'BB':ss[3],
        }
        s='AB'
        def dfs(s):
            if len(s)==N:
                st.add(s)
                return

            for i in range(len(s)-1):
                dfs(s[:i+1]+dic[s[i:i+2]]+s[i+1:])
            
        print(ss)
        for N in range(3,11):
            st=set()
            dfs(s)
            print(N,len(st))
        print('------------')


main()
def main():
    import sys
    N=int(sys.stdin.readline())
    dic={
        'AC':0,
        'WA':0,
        'TLE':0,
        'RE':0,
    }
    for i in range(N):
        S=sys.stdin.readline()
        dic[S.strip()]+=1
    
    for key,val in dic.items():
        print('{} x {}'.format(key,val))

main()
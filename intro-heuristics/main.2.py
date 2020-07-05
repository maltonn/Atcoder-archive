# 各日について、その日のスコアが一番大きくなるようにする
import sys
import numpy as np
def main():
    DEBUG_MODE=True

    if DEBUG_MODE:
        f = open('tester/example/sample2.in')
        fo=open('tester/example/sample2.out','w')
    
    if DEBUG_MODE:
        D = int(f.readline())
    else:
        D = int(sys.stdin.readline())
    Dur = np.zeros(26)
    S = np.zeros((D, 26))
    if DEBUG_MODE:
        C = np.array(list(map(int, f.readline().split())))
    else:
        C = np.array(list(map(int, sys.stdin.readline().split())))

    for i in range(D):
        if DEBUG_MODE:
            S[i] = list(map(int, f.readline().split()))
        else:
            S[i] = list(map(int, sys.stdin.readline().split()))

    for d in range(D):
        Dur += 1
        cand = 0
        score_mx = -10**30
        loss = np.sum(Dur*C)
        for i in range(26):
            sat = S[d, i]
            score = sat+loss - Dur[i]*C[i]
            if score > score_mx:
                score_mx = score
                cand = i


        Dur[cand] = 0
        print(cand+1)  # 1-index
        if DEBUG_MODE:
            fo.write(str(cand+1)+'\n')
    
    if DEBUG_MODE:
        f.close()
        fo.close()
main()

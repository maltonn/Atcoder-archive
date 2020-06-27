#WA

# nが巨大な時

class CMB():
    def __init__(self, mod=10**9+7,mx=5*10**5+1):#mx:入力制限
        N = mx
        g1 = [1, 1]  # 元テーブル
        g2 = [1, 1]  # 逆元テーブル
        inverse = [0, 1]  # 逆元テーブル計算用テーブル
        for i in range(2, N + 1):
            g1.append((g1[-1] * i) % mod)
            inverse.append((-inverse[mod % i] * (mod//i)) % mod)
            g2.append((g2[-1] * inverse[-1]) % mod)
        self.g1 = g1
        self.g2 = g2
        self.mod = mod

    def cmb(self, n, r):  # 素数で割って出力　の場合
        if (r < 0 or r > n):
            return 0
        r = min(r, n-r)
        return self.g1[n] * self.g2[r] * self.g2[n-r] % self.mod

def main():
    C=CMB()
    import sys
    N,M=list(map(int,sys.stdin.readline().split()))
    K=M-N
    r=0
    for l in range(1,K+1):
        r+=C.cmb()*C.cmb(N,l)*C.cmb(N,)
    print(r*C.cmb())



main()
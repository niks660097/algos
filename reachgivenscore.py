# https://practice.geeksforgeeks.org/problems/reach-a-given-score/0


def get_r(r1, i):
    if r1 != -1:
        if r1 is None:
            r1 = [[i]]
        else:
            r1 = [sorted([i] + list(j)) for j in r1]
    return r1


def all_combinations(n, dp):
    if n == 0:
        return None
    if n < 0:
        return -1
    if dp[n]:
        return dp[n]

    r1 = all_combinations(n-3, dp)
    r1 = get_r(r1, 3)
    r2 = all_combinations(n-5, dp)
    r2 = get_r(r2, 5)
    r3 = all_combinations(n-10, dp)
    r3 = get_r(r3, 10)
    r = []
    for R in [r1, r2, r3]:
        if R != -1:
            r += R
    dp[n] = set([tuple(i) for i in r])
    return dp[n]


def main():
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        dp = [0 for i in range(n+1)]
        res = all_combinations(n, dp)
        print(dp)
        print(len(res))

main()

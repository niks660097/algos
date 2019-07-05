# https://practice.geeksforgeeks.org/problems/total-decoding-messages/0


def numdecode(i, L, num_arr, _dict, dp):
    if L == 0:
        return 1
    if i >= L:
        return 1
    if dp[i]:
        return dp[i]

    opt1 = numdecode(i+1, L, num_arr, _dict, dp)

    if i+1 < L and _dict.get(num_arr[i]+num_arr[i+1]):
        opt2 = numdecode(i+2, L, num_arr, _dict, dp)
    else:
        opt2 = 0

    dp[i] = opt1+opt2
    return dp[i]


def main():
    t = int(input())
    _dict = {str(i): True for i in range(27)}
    while t > 0:
        t -= 1
        L = int(input())
        num_arr = [i for i in input()]
        num_arr_no_zero = []
        unsolvable = False
        if num_arr[0] == '0':
            unsolvable = True
        for i in range(L):
            if i+1 < L:
                if num_arr[i] == '0' and num_arr[i+1] == '0':
                    unsolvable = True
                    break
            if num_arr[i] == '0':
                continue
            if i+1 < L and num_arr[i+1] == '0':
                # if _dict.get(num_arr[i]+num_arr[i+1]):
                if int(num_arr[i]) > 2:
                    unsolvable = True
                    break
                num_arr_no_zero.append('X')
                continue
            num_arr_no_zero.append(num_arr[i])
        if unsolvable:
            print('0')
            continue
        break_points = []
        for ind, i in enumerate(num_arr_no_zero):
            if i == 'X':
                break_points.append(ind)
        results = []
        prev_bp = 0
        if not break_points:
            break_points = [len(num_arr_no_zero)]

        for bpind, bp in enumerate(break_points):
            sub_num_arr = num_arr_no_zero[prev_bp:bp]
            _len = len(sub_num_arr)
            dp = [0 for j in range(_len)]
            res = numdecode(0, _len, sub_num_arr, _dict, dp)
            results.append(res)
            if bpind == (len(break_points) - 1):
                sub_num_arr = num_arr_no_zero[bp+1:len(num_arr_no_zero)]
                _len = len(sub_num_arr)
                dp = [0 for j in range(_len)]
                res = numdecode(0, _len, sub_num_arr, _dict, dp)
                results.append(res)
            prev_bp = bp + 1

        final_res = 1
        for i in results:
            final_res *= i
        print(final_res)

main()

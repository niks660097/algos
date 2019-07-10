# https://www.geeksforgeeks.org/snake-ladder-problem-2/
INT_MAX = 0xfffffffffffffff


def lsr(curval, snake, ladder, traversed, bad_nodes, bitten):
    if curval in traversed:
        bad_nodes.append(curval)
        bad_nodes.extend(traversed)
        return 'LOOP'

    if ladder.get(curval):
        traversed.append(curval)
        return lsr(ladder[curval], snake, ladder, traversed, bad_nodes, bitten)

    if snake.get(curval):
        bitten.append(curval)
        traversed.append(curval)
        return lsr(snake[curval], snake, ladder, traversed, bad_nodes, bitten)
    return curval


def mindice(dth, curval, snake, ladder, res, bad_nodes, bitten, dp):
    # print(dth, curval, bitten)
    if curval > 30:
        return None
    if curval in bitten:
        return None
    if curval in bad_nodes:
        return None
    curval = lsr(curval, snake, ladder, [], bad_nodes, bitten)
    if curval == 'LOOP':
        return None
    if curval == 30:
        res.append(dth)
        return dth
    if dp[curval] < INT_MAX and dp[curval] != 0:
        return dp[curval] + dth
    if dp[curval] == INT_MAX:#equivalent to bad nodes
        return None
    # if curval == 30:
    #     res.append(dth)
    #     return dth

    _min_dth = INT_MAX
    for i in range(1, 7):
        rt_val = mindice(dth+1, curval+i, snake, ladder, res, bad_nodes, bitten + [], dp)
        if rt_val is not None:
            _min_dth = min(_min_dth, rt_val-dth)
    dp[curval] = _min_dth
    if dp[curval] < INT_MAX:
        return dp[curval]+dth
    return None


def main():
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        sn_lads = input().split()
        snakes = {}
        ladders = {}
        prev_val = None
        for i in range(2*n):
            val = int(sn_lads[i])
            if prev_val is None:
                prev_val = val
                continue
            if i % 2 != 0:
                if val > prev_val:
                    ladders[prev_val] = val
                elif val < prev_val:
                    snakes[prev_val] = val
            prev_val = val
        res = []#not needed redundant
        # print(snakes, ladders)
        dp = [0 for i in range(31)]
        ans = mindice(0, 1, snakes, ladders, res, [], [], dp)
        print(ans)

main()

def next_big_integer(int_arr):
    if len(int_arr) == 1:
        return int_arr
    ind = len(int_arr)-2
    while ind >= 0:
        if int_arr[ind] < int_arr[ind+1]:
            for j in range(len(int_arr)-1, ind, -1):
                if int_arr[j] > int_arr[ind]:
                    temp = int_arr[ind]
                    int_arr[ind] = int_arr[j]
                    int_arr[j] = temp
                    break
            arr_sect = int_arr[ind+1:]
            arr_sect.sort()
            new_arr = int_arr[:ind+1]+arr_sect
            return new_arr
        ind -= 1
    return int_arr


def main():
    t = int(input())
    while t > 0:
        t -= 1
        _size = input()
        int_arr = input()
        int_arr = [int(i) for i in int_arr.split()]
        res = next_big_integer(int_arr)
        res = [str(i) for i in res]
        print(' '.join(res))

main()
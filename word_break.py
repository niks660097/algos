def word_break(txt, orig_txt, old_decisions, _dict, _ans):
    if not txt:
        if len(''.join(old_decisions)) == len(orig_txt):
            _ans['ans'] = 1
            return
        else:
            return
    ind = 0
    while ind < len(txt):
        possible_word = ''.join(txt[:ind+1])
        if _dict.get(possible_word):
            word_break(txt[ind+1:], orig_txt, old_decisions + [possible_word], _dict, _ans)
            if _ans['ans'] == 1:
                return
        ind += 1


def main():
    t = int(input())
    while t > 0:
        t -= 1
        N = int(input())
        dict_words = input().split()
        orig_txt = list(input())
        _dict = {i: True for i in dict_words}
        _ans = {'ans': 0}
        word_break(orig_txt, orig_txt, [], _dict, _ans)
        print(_ans['ans'])

main()
# -*- coding: utf-8 -*-

import time
from collections import defaultdict


def input_data():
    data = []
    with open('test.txt', encoding='utf-8') as f:
        lines = f.readlines()

        for i in range(0, len(lines), 2):
            cnt = lines[i].strip()
            raw = lines[i + 1].strip()
            data.append([cnt, raw])
    
    return data


def get_sub(raw, even_num):
    data = []
    for i in range(1, len(raw) + 1):
        if sum(raw[:i]) % 2 == even_num:
            data.append(raw[:i])
    if data == []:
        return None
    return data


def solution(cnt, raw):
    cnt = int(cnt)
    raw = list(map(int, raw.split(' ')))
    
    even_num = {}
    odd_num = {}
    
    even_num[0] = get_sub(raw, 0)
    while True:
        before_cnt = len(even_num) + len(odd_num)
        for key, val in even_num.items():
            for v in val:
                nk = key + len(v)
                if odd_num.get(nk) is None:
                    calc = get_sub(raw[nk:], 1)
                    if calc is not None:
                        odd_num[nk] = calc

        for key, val in odd_num.items():
            for v in val:
                nk = key + len(v)
                if even_num.get(nk) is None:
                    calc = get_sub(raw[nk:], 0)
                    if calc is not None:
                        even_num[nk] = calc
        
        if before_cnt == len(even_num) + len(odd_num):
            break

    # print('even_num: ', even_num)
    # print('odd_num:  ', odd_num)


    data = []
    for en in even_num[0]:
        data.append([0, en])

    gcnt = 1
    result = defaultdict(int)
    while True:
        next_data = []
        for key, val in data:
            ncnt = key + len(val)
            if ncnt == cnt:
                result[gcnt] += 1
            else:
                if sum(val) % 2 == 0:
                    if odd_num.get(ncnt) is not None:
                        for on in odd_num[ncnt]:
                            next_data.append([ncnt, on])
                else:
                    if even_num.get(ncnt) is not None:
                        for en in even_num[ncnt]:
                            next_data.append([ncnt, en])

        if next_data == []:
            break

        gcnt += 1
        data = next_data
    
    print(max(result))


if __name__ == '__main__':
    start_time = time.time()
    
    dt = input_data()
    
    for i, (cnt, raw) in enumerate(dt):
        if i < 4:
            solution(cnt, raw)
    
    print('\ntime:', time.time() - start_time)

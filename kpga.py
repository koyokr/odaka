# -*- coding: utf-8 -*-
from random import random, randrange
from typing import List
from plotting import plot


MAXVALUE = 100
N = 30
WEIGHTLIMIT = N*MAXVALUE/4
POOLSIZE = 30
LASTG = 50
MRATE = 0.01
YES = 1
NO = 0

parcel = [[0 for _ in range(2)] for _ in range(N)]
pts1 = set()
pts2 = set()
count1 = 0
GRAPESIZE = 1200
GPL = GRAPESIZE/LASTG


def main() -> int:
    pool = [[0 for _ in range(N)] for _ in range(POOLSIZE)]
    ngpool = [[0 for _ in range(N)] for _ in range(POOLSIZE*2)]
    initparcel()
    initpool(pool)
    for generation in range(1, LASTG+1):
        print('%dth generation' % generation)
        mating(pool, ngpool)
        mutation(ngpool)
        selectng(ngpool, pool)
        printp(pool)
    plot(pts1, GRAPESIZE, 2)
    plot(pts2, GRAPESIZE, 1)
    return 0


def initparcel() -> None:
    global parcel
    for i in range(N):
        parcel[i][0], parcel[i][1] = [int(x) for x in input().split(' ')]


def selectng(ngpool: List[List[int]], pool: List[List[int]]) -> None:
    roulette = [0 for _ in range(POOLSIZE*2)]
    for i in range(POOLSIZE):
        totalfitness = 0
        for c in range(POOLSIZE*2):
            roulette[c] = evalfit(ngpool[c])
            totalfitness += roulette[c]
        ball = randrange(totalfitness)
        acc = 0
        for c in range(POOLSIZE*2):
            acc += roulette[c]
            if acc > ball:
                break
        for j in range(N):
            pool[i][j] = ngpool[c][j]


def selectp(roulette: List[int], totalfitness: int) -> int:
    acc = 0
    ball = randrange(totalfitness)
    for i in range(POOLSIZE):
        acc += roulette[i]
        if acc > ball:
            break
    return i


def mating(pool: List[List[int]], ngpool: List[List[int]]) -> None:
    totalfitness = 0
    roulette = [0 for _ in range(POOLSIZE)]
    for i in range(POOLSIZE):
        roulette[i] = evalfit(pool[i])
        totalfitness += roulette[i]
    for i in range(POOLSIZE):
        while True:
            mama = selectp(roulette, totalfitness)
            papa = selectp(roulette, totalfitness)
            if mama != papa:
                break
        crossing(pool[mama], pool[papa], ngpool[i*2], ngpool[1*2+1])


def crossing(m: List[int], p: List[int], c1: List[int], c2: List[int]) -> None:
    cp = randrange(N)
    for j in range(cp):
        c1[j] = m[j]
        c2[j] = p[j]
    for j in range(cp, N):
        c2[j] = m[j]
        c1[j] = p[j]


def evalfit(g: List[int]) -> int:
    value = 0
    weight = 0
    for pos in range(N):
        weight += parcel[pos][0]*g[pos]
        value += parcel[pos][1]*g[pos]
    if (weight >= WEIGHTLIMIT):
        value = 0
    return value


def printp(pool: List[List[int]]) -> None:
    totalfitness = 0
    elite = 0
    bestfit = 0
    for i in range(POOLSIZE):
        fitness = evalfit(pool[i])
        #print('%s\t%d' % (''.join('%1d' % x for x in pool[i]), fitness))
        if (fitness > bestfit):
            bestfit = fitness
            elite = i
        totalfitness += fitness
    print('%d\t%d \t%lf' % (elite, bestfit, totalfitness/POOLSIZE))
    global count1
    count1 += GPL
    pts1.add(count1 + 1j * bestfit)
    pts2.add(count1 + 1j * totalfitness/POOLSIZE)


def initpool(pool: List[List[int]]) -> None:
    for i in range(POOLSIZE):
        for j in range(N):
            pool[i][j] = randrange(2)


def mutation(ngpool: List[List[int]]) -> None:
    for i in range(POOLSIZE*2):
        for j in range(N):
            if random() <= MRATE:
                ngpool[i][j] = notval(ngpool[i][j])


def notval(v: int) -> int:
    return NO if v == YES else YES


if __name__ == '__main__':
    main()

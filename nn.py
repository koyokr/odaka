# -*- coding: utf-8 -*-
from math import exp
from sys import stdin
from typing import Tuple


INPUTNO = 2
HIDDENNO = 2
MAXINPUTNO = 100


def getdata() -> Tuple[Tuple[float, float], ...]:
    return tuple(tuple(float(s) for s in line.split(' ')[:INPUTNO]) for line in stdin)


def initwh() -> Tuple[Tuple[float, float, float], ...]:
    return ((-2, 3, -1), (-2, 1, 0.5))


def initwo() -> Tuple[float, float, float]:
    return (-60, 94, -1)


def main() -> None:
    wh = initwh()
    wo = initwo()
    e = getdata()
    n_of_e = len(e)
    print('number of data: %d' % n_of_e)



if __name__ == '__main__':
    main()
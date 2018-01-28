#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import random, randint


def addition_exercise(times=5, digits=1, fixed=True, negative=False, negative_proability=0.5):
    numbers = []
    result = 0

    range_max = 10**digits-1
    range_min = 10**(digits-1)

    for i in range(times):
        if fixed:
            n = randint(range_min, range_max)
        else:
            n = randint(1, range_max)

        if negative and random() < negative_proability:
            n = -n

        print(n)

        numbers.append(n)
        result += n

    return numbers, result



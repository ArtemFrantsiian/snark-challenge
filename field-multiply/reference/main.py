#!/usr/bin/env python3

""" Multiply pairs of large integers and report time """

import sys
import json
import time

# large prime int
field_order = int("""
4189849096791895340234421479124063712817070991995394907178350
2921025352812571106773058893763790338921418070971888253786114
3537265295843852015916057220131264689314043479498405430079863
27743462853720628051692141265303114721689601""".replace("\n", ""))


# Mnt4 Fq
class Field:
    def __init__(self, n):
        self.value = n

    def __add__(self, other):
        return Field((self.value + other.value) % field_order)

    def __mul__(self, other):
        return Field((self.value * other.value) % field_order)

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return str(self.value)

def elapsed(message, start_time):
    print ("%s: %0.3fs" % (message, time.time() - start_time))

if __name__ == '__main__':
    start_time = time.time()
    input = json.load(sys.stdin)
    elapsed('json parsing', start_time)

    start_time = time.time()
    data = []
    for pair in input:
        data.append(map(Field, map(int, pair)))
    elapsed('type conversion:', start_time)

    start_time = time.time()
    output = [x * y for [x, y] in data]
    elapsed('math operations:', start_time)

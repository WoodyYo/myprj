#!/usr/bin/env python

from sklearn import svm
from scipy import stats
import os
import sys
from os import listdir
from os.path import join
from cross import *

Emos = ['sad', 'happy', 'angry']

#n = int(sys.argv[1])

def read_mfcc(name):
    f = open(name, 'r')
    while(True):
        s = f.readline()
        if(s[0] == "'"):
            break
    a = s.split(',')[41:548]
    a = [float(i) for i in a]
    a = select(a)
    return a

def select(a):
    global n
    f = [7, 16, 17, 23, 37]
    #f = [n]
    b = []
    for n in f:
        b = b + [a[i*39+n] for i in range(0, 13)]
    return b

def read_energy(name):
    a = []
    f = open(name, 'r')
    for l in f:
        s = l.strip()
        if(s[0] != 'f'):
            a += [float(s.split(';')[2])]
    var = stats.variation(a)

    return [var]*13

value, label = [], []
for emo in Emos:
    for f in listdir(join('data', 'emo_large', emo)):
        mfcc_path = join('data', 'emo_large', emo, f)
        energy_path = join('data', 'energy', emo, f)
        value += [read_energy(energy_path) + read_mfcc(mfcc_path)]
        label += [emo]

cross2(value, label)

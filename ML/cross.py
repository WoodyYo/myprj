from sklearn import svm
from scipy import stats
import os
import sys
from os import listdir
from os.path import join
from learn import get_clf

def cross1(value, label):
    count = 0
    for n in range(0, len(value)):
    	v = value[0:n] + value[n+1:]
    	l = label[0:n] + label[n+1:]
    	
    	clf = get_clf(v, l)
    	a = clf.predict(value[n])
	
    	if(a[0] == label[n]):
            print "=====%s %s=====" %(a, label[n])
            count = count+1
    	else:
            print "%s %s" %(a, label[n])
    print count

def cross2(value, label):
    a = [0, 10, 20, 30, 47, 57, 67, 96, 106]
    a = [i+30 for i in a]
    v, l = [], []
    test_v, test_l = [], []
    for i in range(0, len(value)):
	if i in a:
	    test_v += [value[i]]
	    test_l += [label[i]]
	else:
	    v += [value[i]]
	    l += [label[i]]

    clf = get_clf(v, l)

    for i in range(0, 9):
    	a = clf.predict(test_v[i])
    	if(a[0] == test_l[i]):
            print "=====%s %s=====" %(a, test_l[i])
    	else:
            print "%s %s" %(a, test_l[i])


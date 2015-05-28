#!/usr/bin/env python

from sklearn import svm
from sklearn.mixture import GMM
    
def get_clf(v, l):
    clf = svm.SVC()
    clf.fit(v, l)
    return clf
    #gmm = GMM(n_components=len(v), covariance_type='spherical'
            #init_params='wc', n_iter=20)


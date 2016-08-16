#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

def classify(features_train, labels_train, features_test,labels_test):

    from sklearn.svm import SVC

    from sklearn.metrics import accuracy_score

    clf = SVC(kernel='rbf', C=10000)
    t0 = time()
    # features_train = features_train[:len(features_train) / 100]
    # labels_train = labels_train[:len(labels_train) / 100]
    clf.fit(features_train, labels_train)

    print "training time:", round(time() - t0, 3), "s"
    t1 = time()
    pred = clf.predict(features_test)
    print    pred[10]
    print    pred[26]
    print    pred[50]
    a = 0
    i=0
    while i < len(pred):
        if pred[i]==1:
            a=a+1
        i=i+1
    print a
    print    "training time:", round(time() - t1, 3), "s"
    acuracy = accuracy_score(labels_test, pred)
    print(acuracy)
    return acuracy
#########################################################


print classify(features_train, labels_train, features_test,labels_test)
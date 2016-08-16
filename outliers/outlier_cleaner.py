#!/usr/bin/python

import math

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    diff = []
    diffg = []
    cda = []
    cdn = []
    ### your code goes here
    i=0
    for a in predictions:
        err = math.fabs(a - net_worths[i])
        diff.append(err)
        cleaned_data.append([ages[i],net_worths[i],err])
        i=i+1

    while len(diffg)< len(diff)*0.1:
        diffg.append(max(diff))
        diff.remove(max(diff))

    for z in cleaned_data:
        for h in diffg:
            if math.fabs(z[2])==h:
                cleaned_data.remove(z)


    print cleaned_data
    print len(cleaned_data)
    for n in cleaned_data:
        cda.append(n[1])
        cdn.append(n[2])

    from sklearn import linear_model

    reg = linear_model.LinearRegression()
    reg.fit(cda, cdn)
    # print reg.intercept_
    # print reg.coef_
    # print reg.score(cda, cdn)
    return cleaned_data


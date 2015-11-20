__author__ = 'liu'
import numpy as np
import math
from sklearn.cross_validation import LeaveOneOut
import matplotlib.pyplot as pit

#return the size of the data
def dimension(data):
    row, col = data.shape
    return row, col

# Leave_one_out_cross_validation
def leave_one_out_cross_validation(data, current_set_of_feature, feature_to_add):
    # accuracy = 1
    # current_set_of_feature = [1,2,3]
    distance = 0
    value_num, none = dimension(data)
    print(value_num, none)
    for x in range(value_num):
        print(x)
        for i in current_set_of_feature :
            print(data[x][i])
            distance += pow(data[x][i]-data[x+1][i],2)

    # print(x)
    # print(current_set_of_feature, feature_to_add)
    # print(data[][])
    # return accuracy

# def euclideandistance():


# Forward Selection
def feature_search(data):
    # get the feature number of the feature
    feature = dimension(data)
    # Init the feature sets
    current_set_of_feature = []
    # start from the second col, because the first col is the class
    for i in range(feature-1):

        feature_to_add_at_this_level = []
        best_so_far_accuracy = 0
        print ("On the ", i+1 , "level of the search tree" )
        # try different combination of the features, range start from 0
        for k in range(feature-1):
            # only consider the feature not added
            if not set(current_set_of_feature).intersection([k+1]):
                print("Considering adding the", k+1, "features")
                accuracy = leave_one_out_cross_validation(data, current_set_of_feature, k+1)

            if accuracy > best_so_far_accuracy:
                best_so_far_accuracy = accuracy
                feature_to_add_at_this_level = k+1

        current_set_of_feature.append(feature_to_add_at_this_level)
        print(current_set_of_feature)
        print("On this level",i+1,", i added feature", feature_to_add_at_this_level, "to current set")


def main():

    data = np.genfromtxt('small.txt', delimiter='')
    # feature_search(data)
    leave_one_out_cross_validation(data,[0,2,3],4)

if __name__ == "__main__":
    main()
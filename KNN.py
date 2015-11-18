__author__ = 'liu'
import numpy as np
from sklearn.cross_validation import LeaveOneOut
import matplotlib.pyplot as pit

#Init the feature sets
current_set_of_feature = []

#return the size of the data
def dimension(data):
    row, col = data.shape
    return col

#Leave_one_out_cross_validation
def leave_one_out_cross_validation(data, current_set, feature_to_add):
    accuracy = 0

    return accuracy

def feature_search(data):
    # get the feature number of the feature
    feature = dimension(data)
    # start from the second col because the first col is the class
    for i in range(feature-1):
        feature_to_add_at_this_level = []
        print ("On the ", i+1 , "level of the search tree" )
        # try different combination of the features
        for k in range(feature-1):
            print("Considering adding the", k+1, "features")

loo = LeaveOneOut(4)


def main():

    data = np.genfromtxt('small.txt', delimiter='')
    feature_search(data)

if __name__ == "__main__":
    main()
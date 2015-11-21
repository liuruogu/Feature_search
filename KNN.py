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
def leave_one_out_cross_validation(data, current_set_of_feature):
    N_neighbor = 1
    N_distance = 1000
    distance = 0
    value_num, none = dimension(data)
    count = 0
    for x in range(value_num):# x is the only test set
        # print(x, "test set")
        i = x
        for j in range(value_num): #predict in training set
            if j!=i:
                # print(j,"trainning set")
                for k in current_set_of_feature:
                    # print(x,k,j,k)
                    # print(data[x][k], data[j][k])
                    distance += pow((data[x][k]- data[j][k]),2) # calculate the euclidean distance
                    # print("Distance: ", distance)
                if distance < N_distance :
                    N_distance = distance
                    N_neighbor = j #循环下标+1才是第N个最近邻
                    # print("nearest neighbor", N_neighbor, N_distance)
                    # print("Class of the N_neighbor", data[j][0], data[x][0])
                distance = 0
        if data[N_neighbor][0]==data[x][0]:
            count+=1
            # print("预测准确数", (count/value_num)*100,"%")
        N_distance = 1000
    return (count/value_num)*100
        # print("nearest neighbor", N_neighbor, N_distance)

# Forward Selection
def feature_search(data):
    none, feature = dimension(data)
    current_set_of_feature = []
    best_so_far_accuracy = 0
    feature_to_add_at_this_level = []
    highest_accuracy = 0
    highest_accuracy_feature = []
    for i in range(feature-1):
        current_set_of_feature = [i+1]
        accuracy = leave_one_out_cross_validation(data, current_set_of_feature)
        if accuracy > best_so_far_accuracy:
                best_so_far_accuracy = accuracy
                feature_to_add_at_this_level=i+1
        current_set_of_feature = [feature_to_add_at_this_level]
        print("Using", feature_to_add_at_this_level, "get the highest accuracy is", best_so_far_accuracy, "%")
        highest_accuracy = best_so_far_accuracy
        highest_accuracy_feature = feature_to_add_at_this_level

    for i in range(feature-1):
        feature_to_add_at_this_level = []
        best_so_far_accuracy = 0
        second_feature = current_set_of_feature
        feature_add = []
        for k in range(feature-1):
            if not any([item in [k+1] for item in current_set_of_feature]):
                print("Considering add", k+1, "feature")
                feature_to_add_at_this_level = [k+1]
                second_feature.extend(feature_to_add_at_this_level)
                accuracy = leave_one_out_cross_validation(data, second_feature)
                print("Using", second_feature, "have an accuracy", accuracy, "%")
                second_feature.remove(k+1)
                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    feature_to_add_at_this_level = [k+1]
                    feature_add = feature_to_add_at_this_level

        current_set_of_feature.extend(feature_add)
        if not feature_add == []:
            print("We add feature", feature_add, "at this search level")
            print("At the set", current_set_of_feature, "we have the highest accuracy", best_so_far_accuracy,"%")
            print()
        if best_so_far_accuracy > highest_accuracy:
            highest_accuracy = best_so_far_accuracy
            highest_accuracy_feature = current_set_of_feature
        print("Finished search! The best feature subset is", highest_accuracy_feature,"which has an accuracy of", highest_accuracy,"%")
def main():

    data = np.genfromtxt('small.txt', delimiter='')
    feature_search(data)

if __name__ == "__main__":
    main()
__author__ = 'liu'
import numpy as np
import copy
import math


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
    for x in range(value_num):  # x is the only test set
        i = x
        for j in range(value_num):  # predict in training set
            if j != i:
                for k in current_set_of_feature:
                    distance += pow((data[x][k] - data[j][k]), 2)  # calculate the euclidean distance
                if distance < N_distance:
                    N_distance = distance
                    N_neighbor = j
                distance = 0
        if data[N_neighbor][0] == data[x][0]:
            count += 1
        N_distance = 1000
    return (count / value_num) * 100


# Forward Selection
def feature_search(data):
    none, feature = dimension(data)
    current_set_of_feature = []
    best_so_far_accuracy = 0
    feature_to_add_at_this_level = []
    highest_accuracy = 0
    highest_accuracy_feature = []
    second_feature = []
    for i in range(feature - 1):
        current_set_of_feature = [i + 1]
        accuracy = leave_one_out_cross_validation(data, current_set_of_feature)
        if accuracy > best_so_far_accuracy:
            best_so_far_accuracy = accuracy
            feature_to_add_at_this_level = i + 1
        current_set_of_feature = [feature_to_add_at_this_level]
        print("Using", feature_to_add_at_this_level, "get the highest accuracy is", best_so_far_accuracy, "%")

    for i in range(feature - 1):
        feature_to_add_at_this_level = []
        best_so_far_accuracy = 0
        second_feature = current_set_of_feature
        feature_add = []
        for k in range(feature - 1):
            if not any([item in [k + 1] for item in current_set_of_feature]):  # consider features not added yet
                print("Considering add the", k + 1, "feature")
                feature_to_add_at_this_level = [k + 1]
                second_feature.extend(feature_to_add_at_this_level)
                accuracy = leave_one_out_cross_validation(data, second_feature)
                print("Using", second_feature, "have an accuracy", accuracy, "%")
                second_feature.remove(k + 1)
                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    feature_to_add_at_this_level = [k + 1]
                    feature_add = feature_to_add_at_this_level

        current_set_of_feature.extend(feature_add)
        if not feature_add == []:
            print("We add feature", feature_add, "at this search level")
            print("At the set", current_set_of_feature, "we have the highest accuracy", best_so_far_accuracy, "%")
            print()
        if highest_accuracy < best_so_far_accuracy:
            print("!!!!At the highest_set", highest_accuracy_feature, "we have the highest accuracy", highest_accuracy,
                  "got beat up!!")
            highest_accuracy_feature = copy.copy(current_set_of_feature)
            print("!!!!I got the highest accuracy features as follow", highest_accuracy_feature)
            print("-----Hightest accurcy so far feature set is", highest_accuracy_feature)
            highest_accuracy = best_so_far_accuracy

    print("Finished search! The best feature subset is", highest_accuracy_feature, "which has an accuracy of",
          highest_accuracy, "%")


# Backward eliminiation
def Backward_search(data):
    '''Get the feature number of the date set'''
    none, feature = dimension(data)
    current_set_of_feature = []
    best_so_far_accuracy = 0
    highest_eliminated_set = []
    highest_accuracy = 0
    highest_accuracy_feature = []

    '''initialize the feature set'''
    for each in range(1, feature):
        print(each)
        current_set_of_feature.append(each)

    '''eliminate feature-1 times of features'''
    for each in range(1, feature - 1):

        intermedia_set = copy.copy(current_set_of_feature)
        for each in intermedia_set:
            intermedia_set.remove(each)
            print("Using features", intermedia_set)
            accuracy = leave_one_out_cross_validation(data, intermedia_set)
            if accuracy > best_so_far_accuracy:
                best_so_far_accuracy = accuracy
                print("set", intermedia_set, "have highest accuracy", best_so_far_accuracy)
                highest_eliminated_set = copy.copy(intermedia_set)
                print("The highest eliminated set is", highest_eliminated_set)
            intermedia_set = copy.copy(current_set_of_feature)
        if best_so_far_accuracy > highest_accuracy:
            highest_accuracy = best_so_far_accuracy
            highest_accuracy_feature = copy.copy(highest_eliminated_set)
        best_so_far_accuracy = 0
        print("--------The highest eliminated set is", highest_eliminated_set)
        current_set_of_feature = copy.copy(highest_eliminated_set)

    print("We found the best test sets so far is", highest_accuracy_feature, "Have highest accuracy", highest_accuracy,
          "%")

    return 0


def Faster_search_algorithm(data):
    '''KNN are sensitive to irrelevant feature, try to use less irrelevant feature'''
    none, feature = dimension(data)
    current_set_of_feature = []
    best_so_far_accuracy = 0
    feature_to_add_at_this_level = []
    highest_accuracy = 0
    highest_accuracy_feature = []
    second_feature = []
    for i in range(feature - 1):
        current_set_of_feature = [i + 1]
        accuracy = leave_one_out_cross_validation(data, current_set_of_feature)
        if accuracy > best_so_far_accuracy:
            best_so_far_accuracy = accuracy
            feature_to_add_at_this_level = i + 1
        current_set_of_feature = [feature_to_add_at_this_level]
        print("Using", feature_to_add_at_this_level, "get the highest accuracy is", best_so_far_accuracy, "%")

    for i in range(feature - 1):
        feature_to_add_at_this_level = []
        best_so_far_accuracy = 0
        second_feature = current_set_of_feature
        feature_add = []
        for k in range(feature - 1):
            if not any([item in [k + 1] for item in current_set_of_feature]):  # consider features not added yet
                print("Considering add the", k + 1, "feature")
                feature_to_add_at_this_level = [k + 1]
                second_feature.extend(feature_to_add_at_this_level)
                accuracy = leave_one_out_cross_validation(data, second_feature)
                print("Using", second_feature, "have an accuracy", accuracy, "%")
                second_feature.remove(k + 1)
                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    feature_to_add_at_this_level = [k + 1]
                    feature_add = feature_to_add_at_this_level

        current_set_of_feature.extend(feature_add)
        if highest_accuracy < best_so_far_accuracy:
            print("!!!!At the highest_set", highest_accuracy_feature, "we have the highest accuracy", highest_accuracy,
                  "got beat up!!")
            highest_accuracy_feature = copy.copy(current_set_of_feature)
            print("!!!!I got the highest accuracy features as follow", highest_accuracy_feature)
            print("-----Hight accurcy feature set is", highest_accuracy_feature)
            highest_accuracy = best_so_far_accuracy
        elif highest_accuracy >= best_so_far_accuracy:
            break
    print("Finished search! The best feature subset is", highest_accuracy_feature, "which has an accuracy of",
          highest_accuracy, "%")


def main():
    '''Get the feature number of the date set'''
    # print("Welcome to Ruogu's Feature Selection Algorithm")
    file = input("Type the name of the file to test ")
    data = np.genfromtxt(file, delimiter='')

    print("1) Forward Selection 2)Backward Selection 3)Ruogu's Special algorithm")
    Algorithm_select = input("Type the number of the algorithm you want to run ")

    if Algorithm_select == '1':
        feature_search(data)
    elif Algorithm_select == '2':
        Backward_search(data)
    elif Algorithm_select == '3':
        Faster_search_algorithm(data)


if __name__ == "__main__":
    main()

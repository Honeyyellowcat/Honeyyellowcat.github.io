"""
* Name:
* Date:
* CSE 160, Spring 2024
* Homework 4
* Description:
* Collaboration:
"""

from utils import load_centroids, read_data
from kmeans import get_closest_centroid  # noqa: F401


# ----------------------------------------------------------
# PROBLEMS FOR STUDENTS
def assign_labels(list_of_points, labels, centroids_dict):
    """
    Assign all data points to the closest centroids and keep track of their
    labels. The i-th point in "data" corresponds to the i-th label in "labels".

    Arguments:
        list_of_points: a list of lists representing all data points
        labels: a list of ints representing all data labels
                labels[i] is the label of the point list_of_points[i]
        centroids_dict: a dictionary representing the centroids where the keys
                        are strings (centroid names) and the values are lists
                        of centroid locations

    Returns: a new dictionary whose keys are the centroids' key names and
             values are a list of labels of the data points that are assigned
             to that centroid.

    Example:
        Code:
            list_of_points = [[1.1, 1, 1, 0.5], [4, 3.14, 2, 1], [0, 0, 0, 0]]
            labels = [2, 1, 3]
            centroids_dict = {"centroid1": [1, 1, 1, 1],
                              "centroid2": [2, 2, 2, 2]}
            print(assign_labels(list_of_points, labels, centroids_dict))
        Output:
            {'centroid1': ['M', 'N'], 'centroid2': ['W']}
    """

    assignments = {centroid: [] for centroid in centroids_dict}
    
    for point, label in zip(list_of_points, labels):
        closest_centroid = get_closest_centroid(point, centroids_dict)
        assignments[closest_centroid].append(label)
    
    return assignments
    pass


def majority_count(labels):
    """
    Return the count of the majority labels in the label list

    Arguments:
        labels: a list of labels

    Returns: the count of the majority labels in the list
    """

    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
    
    majority_label = max(counts, key=counts.get)
    return counts[majority_label]
    pass


def accuracy(list_of_points, labels, centroids_dict):
    """
    Calculate the accuracy of the algorithm. You should use assign_labels and majority_count (that
    you previously implemented)

    Arguments:
        list_of_points: a list of lists representing all data points
        labels: a list of ints representing all data labels
                labels[i] is the label of the point list_of_points[i]
        centroids_dict: a dictionary representing the centroids where the keys
                        are strings (centroid names) and the values are lists
                        of centroid locations

    Returns: a float representing the accuracy of the algorithm
    """

    assignments = assign_labels(list_of_points, labels, centroids_dict)
    correct_count = sum(majority_count(labels) for labels in assignments.values())
    total_count = len(labels)
    
    return correct_count / total_count
    pass


if __name__ == "__main__":
    centroids = load_centroids("mnist_final_centroids.csv", with_key=True)
    # Consider exploring the centroids data here

    data, label = read_data("data/mnist.csv")
    print(accuracy(data, label, centroids))

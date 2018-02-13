import os
from sys import platform
import json
import numpy as np

# Returns the Euclidean distance score between user1 and user2
def euclidean_score(dataset, user1, user2):
    # Check user in dataset.
    if user1 not in dataset: raise Exception('User ' + user1 + ' not in dataset.')
    if user2 not in dataset: raise Exception('User ' + user2 + ' not in dataset')
    rated_by_both = {item:1 for item in dataset[user1] if item in dataset[user2]}

    if len(rated_by_both) == 0: return 0
    squared_differences = [np.square(dataset[user1][item] - dataset[user2][item]) for item in dataset[user1] if item in dataset[user2]]

    return 1 / (1 + np.sqrt(np.sum(squared_differences)))

if __name__=='__main__':
    path = os.path.dirname(os.getcwd())

    filename = path + '/data_files/movie_ratings.json' \
        if platform == 'linux' or platform == 'linux2' \
        else path + '\\data_files\\movie_ratings.json'

    with open(filename, 'r') as f: data = json.loads(f.read())
    user1 = 'Rajan'
    user2 = 'Rinku'

    print('\nEuclidean score:')
    print(euclidean_score(data, user1, user2))

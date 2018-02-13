import os
from sys import platform
import json
import numpy as np

# Returns the Pearson correlation score between user1 and user2
def pearson_score(dataset, user1, user2):
    if user1 not in dataset: raise Exception('User ' + user1 + ' not in dataset.')
    if user2 not in dataset: raise Exception('User ' + user2 + ' not in dataset')

    # Movies rated by both user1 and user2
    rated_by_both = {item: 1 for item in dataset[user1] if item in dataset[user2]}
    if len(rated_by_both) == 0: return 0
    num_ratings = len(rated_by_both)

    # Compute the sum of ratings of all the common preferences
    user1_sum = np.sum([dataset[user1][item] for item in rated_by_both])
    user2_sum = np.sum([dataset[user2][item] for item in rated_by_both])

    # Compute the sum of squared ratings of all the common preferences
    user1_squared_sum = np.sum([np.square(dataset[user1][item]) for item in rated_by_both])
    user2_squared_sum = np.sum([np.square(dataset[user2][item]) for item in rated_by_both])

    # Compute the sum of products of the common ratings
    product_sum = np.sum([dataset[user1][item] * dataset[user2][item] for item in rated_by_both])

    # Compute the Pearson correlation
    Sxy = product_sum - (user1_sum * user2_sum / num_ratings)
    Sxx = user1_squared_sum - np.square(user1_sum) / num_ratings
    Syy = user2_squared_sum - np.square(user2_sum) / num_ratings

    if Sxx * Syy == 0: return 0

    return Sxy / np.sqrt(Sxx * Syy)

if __name__=='__main__':
    path = os.path.dirname(os.getcwd())

    filename = path + '/data_files/movie_ratings.json' \
        if platform == 'linux' or platform == 'linux2' \
        else path + '\\data_files\\movie_ratings.json'

    with open(filename, 'r') as f:
        data = json.loads(f.read())

    user1 = 'Rajan'
    user2 = 'Rinku'

    print('\nPearson score:')
    print( pearson_score(data, user1, user2))

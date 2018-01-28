# -------------------------------------------------
# Classifies data into 2 classes. If in point(x, y)
#  case 1. x > y  : class_A
#  case 2. x < y  : class_B
# --------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# input data
X = np.array([[3,1], [2,5], [1,8], [6,4], [5,2], [3,5], [4,7], [4,-1]])

# labels
y = [0, 1, 1, 0, 0, 1, 1, 0]

# separate the data into classes based on 'y'.
# e.g First value in X is [3, 1] 3 > 1 and classified in y as 0 and so on
class_A = np.array([X[i] for i in range(len(X)) if y[i] == 0])
class_B = np.array([X[i] for i in range(len(X)) if y[i] == 1])

# draw the separator line, seperates data points in to two classes
line_x = range(10)
line_y = line_x

# plot labeled data and separator line
plt.figure()
plt.scatter(class_A[:, 0], class_A[:, 1], color='red', marker='s')
plt.scatter(class_B[:,0], class_B[:,1], color='green', marker='x')
plt.plot(line_x, line_y, color='blue', linewidth=3)
plt.show()

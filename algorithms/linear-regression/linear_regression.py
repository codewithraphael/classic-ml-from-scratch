import numpy as np
import seaborn as sns; sns.set_theme()
import matplotlib.pyplot as plt

class LinearRegression:

    def fit(self, X, y, intercept=False):

        # record data and dimension
        if intercept == False: # add intercept (if not already included)
            ones = np.ones(len(X), axis = 1)
        self.X = np.array(X)
        self.y = np.array(y)
        self.N, self.D = self.X.shape

        # estimate parameters
         
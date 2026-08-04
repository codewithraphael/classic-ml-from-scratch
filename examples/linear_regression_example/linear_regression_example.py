import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set_theme()

# =========================
# GENERATING DATA 
# =========================

np.random.seed(123)
N = 20
beta0 = -4
beta1 = 2

x = np.random.randn(N)
e = np.random.randn(N)
y = beta0 + beta1 * x + e

true_x = np.linspace(min(x), max(x), N)
true_y = beta0 + beta1 * true_x

# =========================
#  PLOT
# =========================

fig, ax = plt.subplots()
sns.scatterplot(x = x, y = y, s=40, label='data')
sns.lineplot(x = true_x, y = true_y, color='red', label='true model')
ax.set_xlabel('x', fontsize=14)
ax.set_title(fr"$y = {beta0} + ${beta1}$x + \epsilon$", fontsize =16)
ax.set_ylabel('y', fontsize=14, rotation = 0, labelpad=10)
ax.legend(loc=4)
sns.despine()
plt.savefig('linear_regression_example_plot.png')
plt.close()

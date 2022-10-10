import matplotlib.pyplot as plt
import numpy as np

mu = 5
sigma = 0.5
s = np.random.normal(size=1000, loc=mu, scale=sigma)
print(s)

count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) *
         np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)),
         linewidth=2, color='r')
plt.xlabel('Schaden durch Zombie', fontsize=18)
plt.ylabel('Häufigkeit', fontsize=16)
plt.xlim((0, 8))
plt.show()

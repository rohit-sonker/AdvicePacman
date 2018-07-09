import numpy as np
import matplotlib.pyplot as plt

fname = ('trdata-7-6-15-39-16.csv')
pathname = ('/home/starshipcrew/results/noadvice/')
epi, score = np.loadtxt(pathname+fname,unpack = 1, delimiter = ',' )
plt.plot(epi, score , 'b-')

plt.xlabel('Training Episodes')
plt.ylabel('Reward')
plt.title('Rewards accumulated - No Advice')
plt.axis([0, len(epi), -1000,1000 ])
plt.grid(True)
plt.show()

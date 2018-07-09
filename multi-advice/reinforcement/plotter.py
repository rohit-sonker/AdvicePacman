import numpy as np
import matplotlib.pyplot as plt

fname = ('')
pathname = ('/home/starshipcrew/results/singleadvice/')
epi, score = np.loadtxt(pathname+fname,unpack = 1, delimiter = ',' )
plt.plot(epi, score , 'b-')

plt.xlabel('Training Episodes')
plt.ylabel('Reward')
plt.title('Rewards accumulated - Single Advice')
plt.axis([0, len(epi), -1000,1000 ])
plt.grid(True)
plt.show()

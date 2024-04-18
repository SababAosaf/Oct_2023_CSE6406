import pickle
import random

import numpy as np
from matplotlib import pyplot as plt

ip=1

dbfile = pickle.load(open('T1123', 'rb'))
print(dbfile)

for ij in dbfile:
    print(ij)
    c='#'
    if ip==1 or ip==100 :
        for i in range(0,6):
            c=c+random.choice(['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'])

        lists=ij

        plt.scatter(np.array(lists)[: , 0], np.array(lists)[:,1], s=ip, facecolors=c, edgecolors=c,label=str(ip)+'th Iteration')

    ip=ip+1

plt.title("Protein T1123")
plt.xlabel("Energy")
plt.ylabel("1/Contact_Score")
plt.subplots_adjust(bottom=0.15, left=.2)
plt.legend()
plt.show()

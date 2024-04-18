import pickle
import random
from operator import itemgetter

import numpy as np
from matplotlib import pyplot as plt
from pymoo.indicators.hv import HV

ip=1
protein='T1123'
dbfile = pickle.load(open(protein, 'rb'))


e=999999999
i=999999999
e1=-9999999999999
i1=-9999999999


for ij in dbfile:
    for solution in ij:

        if solution[0]<e:
            e=solution[0]
        if solution[0]>e1:
            e1=solution[0]
        if solution[1]<i:
            i=solution[1]
        if solution[1]>i1:
            i1=solution[1]



f=[]
n1=-99999999999
n2=-9999999


for ij in dbfile:
    fps=[]
    for solution in ij:
        ip=solution[0]
        if ip>n1:
            n1=ip
        jp=(solution[1]-i)/(i1-i)
        if jp>n2:
            n2=jp

        fps.append([ip,jp])
    f.append(fps)




ipj=1
lists=[]

energies=[]
contact=[]
for ijk in f:
    l=ijk
    l=sorted(l,key=itemgetter(0))
    en=l[0][0]
    energies.append([ipj,en])
    contact.append([ipj,l[len(l)-1][0]])
    # ip=0
    # area=0
    # for point in l:
    #     height=n2-point[1]
    #
    #     if ip==len(l)-1:
    #         width=n1-point[0]
    #     else:
    #         width=l[ip+1][0]-point[0]
    #     ip=ip+1
    #
    #     area=area+height*width
    if ipj==100:
        print([en])
        print(l[0][1])
        print(l[len(l)-1][0])
        print(l[len(l)-1][1])



    # lists.append([ipj,area])
    #
    ipj=ipj+1


x = np.array(energies)[: , 0]  # X-axis points
y = np.array(energies)[:,1] # Y-axis points
plt.xlabel("Iteration")
plt.ylabel("Energies")
plt.title("Protein "+protein)
plt.plot(x, y,'r')  # Plot the chart


x = np.array(contact)[: , 0]  # X-axis points
y = np.array(contact)[:,1] # Y-axis points

plt.plot(x, y,'b')  # Plot the chart



plt.show()


# plt.title("Protein T1123")
# plt.xlabel("Energy")
# plt.ylabel("1/Contact_Score")
# plt.subplots_adjust(bottom=0.15, left=.2)
# plt.legend()
# plt.show()

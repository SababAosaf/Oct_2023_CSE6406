import inspect
import pickle
import random
import string
import numpy as np
from matplotlib import pyplot as plt
from pymoo.algorithms.soo.nonconvex.pso import PSO
from pymoo.core import problem
from pymoo.factory import get_problem
from pymoo.util.display.column import Column
from pymoo.util.display.output import Output
from pymoo.visualization.scatter import Scatter

from MyMutation import MyMutation
from  MyProblem import MyProblem
from pymoo.algorithms.moo.nsga2 import NSGA2
import pymoo.optimize as optimize
from duplicates import MyDuplicateElimination
from CR import MyCrossover
from initialization import MySampling
print("START")



class MyOutput(Output):

    def __init__(self):
        super().__init__()


    def update(self, algorithm):
        super().update(algorithm)
        print(algorithm.pop.get("X"))


if __name__=='__main__':
    algorithm = NSGA2(pop_size=50,
                      sampling=MySampling(),
                      crossover=MyCrossover(),
                      mutation=MyMutation(),eliminate_duplicates=False,save_history=True
                     )

    plt.figure(figsize=(7, 5))

    protein_name='T1137s2-D2'

    protein_path='casp15\\'+protein_name
    stat_path=protein_path

    contact_path='native_structures\\T1137s2-D2.pdb'

    init_path=protein_path


    problem_1=MyProblem('casp15\\'+protein_name,stat_path,contact_path,init_path)
    print("POLO")
    res = optimize.minimize(problem_1,
                   algorithm,
                   ('n_gen', 20 ),
                   seed=1, output=MyOutput(),
                   verbose=True)

    lists1=[]

    for ij in res.history:
        lists11=[]
        for k in ij.opt:
            lists11.append(k.F.tolist())
        lists1.append(lists11)

    dbfile = open(protein_name, 'wb')
    pickle.dump(lists1,dbfile)
    dbfile.close()


    # ip=1
    #
    # dbfile = open('proteins', 'wb')
    # pickle.dump(res,dbfile)
    # dbfile.close()
    #
    # for ij in res.history:
    #     print("H")
    #     c='#'
    #     if True : #ip%10==0:
    #         for i in range(0,6):
    #             c=c+random.choice(['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'])
    #
    #         lists=[]
    #
    #         for k in ij.opt:
    #             lists.append(k.F.tolist())
    #         print(lists)
    #
    #         plt.scatter(np.array(lists)[: , 0], np.array(lists)[:,1], s=ip, facecolors=c, edgecolors=c,label=str(ip)+'th Iteration')
    #
    #     ip=ip+1
    #
    # plt.title("Objective Space")
    # plt.legend()
    # plt.show()
    # n_evals = np.array([e.evaluator.n_eval for e in res.history])
    # opt = np.array([e.opt[0].F for e in res.history])
    #
    # plt.title("Convergence")
    # plt.plot(n_evals, opt, "--")
    # plt.yscale("log")
    # plt.show()

    # pf_a, pf_b = problem_1.pareto_front(use_cache=False, flatten=False)
    # pf = problem_1.pareto_front(use_cache=False, flatten=True)
    # plt.plot(pf_a[:, 0], pf_a[:, 1], alpha=0.5, linewidth=2.0, color="red", label="Pareto-front")
    # plt.plot(pf_b[:, 0], pf_b[:, 1], alpha=0.5, linewidth=2.0, color="red")

    # plt.scatter(res.F[:, 0], res.F[:, 1], s=30, facecolors='none', edgecolors='b', label="Solutions")
    # plt.title("Objective Space")
    # plt.legend()
    # plt.show()


    # print(res.pf)
    # plot.add(res.pf, facecolor="none", edgecolor="red")
    # plot.show()
    # print("RESULTS")
    # print(res)

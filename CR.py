import random
from random import randrange

from pymoo.core.crossover import Crossover
import numpy as np

import protein_operators
import valueGenerator
import math


import random

from Bio.PDB import Superimposer
from Bio.PDB.Atom import Atom
from deap.tools import cxSimulatedBinary

import copy

class MyCrossover(Crossover):

    def __init__(self, prob=0.5, **kwargs):
        super().__init__(2, 2, **kwargs)
        self.prob = prob

    def _do(self, problem, X, **kwargs):


        _X = np.copy(X)

        for i in range(len(_X[0])):

            list1=copy.deepcopy(_X[0][i][0])
            list2= copy.deepcopy(_X[1][i][0])

            r=random.choice([0,1])

            if r==1:

                (list1,list2)=protein_operators.crossover(list1,list2)

            _X[0][i][0]=list1
            _X[1][i][0]=list2

        return _X



import os
import random
import time
from operator import itemgetter

import numpy
import numpy as np
import tmscoring
from Bio.PDB import PDBIO
from pymoo.core.parameters import flatten
from pymoo.core.problem import ElementwiseProblem
from pymoo.util.misc import stack

import contactMap
import energyFromPDBPath


class MyProblemTM(ElementwiseProblem):

    allows=[]
    contact=[]
    native_sequence=''
    native_sequence_path=''
    def __init__(self,folder,stat_path,contacts_path,initialization_path,native_protein_path):
        super().__init__(n_var=1, n_obj=1, n_ieq_constr=0)

        self.folder=folder
        self.stat_path=stat_path
        self.contact_path=contacts_path
        self.init_path=initialization_path
        self.native_sequence_path=native_protein_path

    def LongC(self,st1, st2):
      ans = 0
      s1,s2,k1=0,0,0
      for a in range(len(st1)):
             for b in range(len(st2)):
                k = 0
                while ((a + k) < len(st1) and (b + k) < len(st2)
            and st1[a + k] == st2[b + k]):
                    k = k + 1
                if k>ans:
                    s1=a
                    s2=b
                    k1=k
                ans = max(ans, k)


      return (s1,s2,k1)

    def _calc_pareto_front(self, flatten=False, *args, **kwargs):
        f2 = lambda f1: ((f1/100) ** 0.5 - 1)**2
        F1_a, F1_b = np.linspace(1, 16, 300), np.linspace(36, 81, 300)
        F2_a, F2_b = f2(F1_a), f2(F1_b)

        pf_a = np.column_stack([F1_a, F2_a])
        pf_b = np.column_stack([F1_b, F2_b])

        return stack(pf_a, pf_b, flatten=flatten)

    def _calc_pareto_set(self, *args, **kwargs):
        x1_a = np.linspace(0.1, 0.4, 50)
        x1_b = np.linspace(0.6, 0.9, 50)
        x2 = np.zeros(50)

        a, b = np.column_stack([x1_a, x2]), np.column_stack([x1_b, x2])
        return stack(a,b, flatten=flatten)

    def _evaluate(self, x, out, *args, **kwargs):

        protein_structure=  x[0]

        io = PDBIO()
        io.set_structure(protein_structure)
        io.save('pdb\\checkTM.pdb')

        print("TM COMPARISON")
        try:
            alignment = tmscoring.TMscoring('pdb\\checkTM.pdb',  self.native_sequence_path)
            alignment.optimise()
            tm_score=alignment.tmscore(**alignment.get_current_values())
            print(tm_score)
            tm_score=1/tm_score
        except Exception:
            tm_score=1/0.1

        out["F"] = np.array([tm_score], dtype=float)


        # out["G"]=200-influencial


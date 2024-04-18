import os
import random
import time
from operator import itemgetter

import numpy
import numpy as np
from Bio.PDB import PDBIO
from pymoo.core.parameters import flatten
from pymoo.core.problem import ElementwiseProblem
from pymoo.util.misc import stack

import contactMap
import energyFromPDBPath


class MyProblem(ElementwiseProblem):

    allows=[]
    contact=[]
    native_sequence=''
    def __init__(self,folder,stat_path,contacts_path,initialization_path):
        super().__init__(n_var=1, n_obj=2, n_ieq_constr=0)

        self.folder=folder
        self.stat_path=stat_path
        self.contact_path=contacts_path
        self.init_path=initialization_path

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
        d3to1 = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
         'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N',
         'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
         'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}

        # print the current timestamp

        energy, contact = 0, 0
        print(x)
        protein_structure=  x[0]
        print(protein_structure)
        print("THIS")
        io = PDBIO()
        print(os.getcwd())
        io.set_structure(protein_structure)
        io.save('pdb\\check.pdb')
        ## ASYSNC IO
        energy=energyFromPDBPath.energyFromPDBPath('pdb\\check.pdb')
        os.remove('pdb\\check.pdb')
        print([energy])

        contacts_1=contactMap.currentContactMap(protein_structure)


        s=''
        for model in protein_structure:
         for chain in model:
             seq = []
             for residue in chain:
                 seq.append(d3to1[residue.resname])
                 s=''.join(seq)

        current=self.contact
        s1=self.LongC(s,self.native_sequence)
        print(self.LongC(s,self.native_sequence))
        print(s)
        print(self.native_sequence)
        print(s[s1[0]:s1[2]+s1[0]])
        contacts_1=contacts_1[s1[0]:s1[2]+s1[0],s1[0]:s1[2]+s1[0]]
        contacts_1[contacts_1<12]=1
        contacts_1[contacts_1!=1]=0
        current=current[s1[1]:s1[2]+s1[1],s1[1]:s1[2]+s1[1]]

        print(contacts_1)
        print(current)
        scores=0
        for i in range(contacts_1.shape[0]):
            for j in range(contacts_1.shape[1]):
                if contacts_1[i][j]==current[i][j] :
                    scores=scores+0.01

        scores=1/scores
        # score=numpy.subtract(contacts_1,current)
        # scores=0
        #
        # for ijk in score:
        #     for jj in ijk:
        #         scores=(scores+jj)/1000

        print("Contact Score: "+str(scores))
        print("Energy: "+str(energy))

        out["F"] = np.array([energy,scores], dtype=float)
        # out["G"]=200-influencial


import os
import pickle


import pickle

import numpy as np
import tmscoring
from Bio.PDB import PDBIO
from matplotlib import pyplot as plt

import energyFromPDBPath


class CustomUnpickler(pickle.Unpickler):

    def find_class(self, module, name):
        if name == 'MyOutput':
            from NSGAII import MyOutput
            return MyOutput
        return super().find_class(module, name)


def analyze_history():
    i=0
    pickle_data = CustomUnpickler(open('history\\proteins', 'rb')).load()
    for iteration in pickle_data.history:
        for j in iteration.opt:
            structures=j.X[0]
            io = PDBIO()
            io.set_structure(structures)
            p_path='history\\pdb2\\'+str(i)+'.pdb'
            io.save('history\\pdb2\\'+str(i)+'.pdb')
            energy=energyFromPDBPath.energyFromPDBPath(p_path)


            i=i+1

    n_evals = np.array([e.evaluator.n_eval for e in pickle_data.history])
    opt = np.array([e.opt[0].F for e in pickle_data.history])

    plt.title("Convergence")
    plt.plot(n_evals, opt, "--")
    plt.yscale("log")
    plt.show()


def analyze_history():
    i=0
    pickle_data = CustomUnpickler(open('history\\proteins', 'rb')).load()
    for iteration in pickle_data.history:
        for j in iteration.opt:
            structures=j.X[0]
            io = PDBIO()
            io.set_structure(structures)
            p_path='history\\pdb\\'+str(i)+'.pdb'
            io.save('history\\pdb\\'+str(i)+'.pdb')
            energy=energyFromPDBPath.energyFromPDBPath(p_path)


            i=i+1

    n_evals = np.array([e.evaluator.n_eval for e in pickle_data.history])
    opt = np.array([e.opt[0].F for e in pickle_data.history])

    plt.title("Convergence")
    plt.plot(n_evals, opt, "--")
    plt.yscale("log")
    plt.show()

def analyze_pdb():
    path='history\\pdb'
    files=os.listdir(path)
    energy_lists=[]
    protein_serials=[]
    for ijk in files:

        energies=energyFromPDBPath.energyList(path+'\\'+ijk)
        print(energies)
        energy_lists.append(energies)
        ij=ijk[0:ijk.index('.')]
        protein_serials.append(ij)
    line=''
    ijp=0
    for ij in energy_lists[0]:
        line=line+','+ij[0]
    line='serial'+line
    line1=''
    for j in energy_lists:
        line1=''
        for k in j:
            line1=line1+','+k[1]
        line=line+'\n'+str(ijp)+''+line1
        ijp=ijp+1

    print(line)

def analyze_pdb_TM(path):
    path='history\\pdb2'
    files=os.listdir(path)
    energy_lists=[]
    protein_serials=[]
    for ijk in files:

        try:
            alignment = tmscoring.TMscoring('pdb2\\'+ijk,  path)
            alignment.optimise()
            tm_score=alignment.tmscore(**alignment.get_current_values())
            print(tm_score)
            tm_score=1/tm_score
            energy_lists.append(("TM",str(tm_score)))
            ij=ijk[0:ijk.index('.')]
            protein_serials.append(ij)
        except Exception:
            tm_score=1/0.1
    line=''
    ijp=0
    for ij in energy_lists[0]:
        line=line+','+ij[0]
    line='serial'+line
    line1=''
    for j in energy_lists:
        line1=''
        for k in j:
            line1=line1+','+k[1]
        line=line+'\n'+str(ijp)+''+line1
        ijp=ijp+1

    print(line)
analyze_history()

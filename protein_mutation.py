
import random
import copy

import numpy as np
from Bio.PDB.Atom import Atom


def mutate(protein_structure):
    protein_structure=copy.deepcopy(protein_structure)
    count=0
    ij=0
    for model in protein_structure:
        a = model.id
        for chain in model:
            b = chain.id
            for residue in chain:
                c=residue.id
                for atom in residue:

                    e=atom.id
                    coord=atom.get_coord()

                    (a1,b1,c1)=all_random(0.5,0.1)
                    Atom.set_coord(protein_structure[a][b][c][e], (coord[0]+a1, coord[1]+b1, coord[2]+c1))
                    count=count+1

    return protein_structure
def mutate1(protein_structure, allowed):
    protein_structure=copy.deepcopy(protein_structure)
    count=0
    ij=0
    for model in protein_structure:
        a = model.id
        for chain in model:
            b = chain.id
            for residue in chain:
                c=residue.id
                for atom in residue:
                    if ij in allowed or 0.9<random.random():
                        e=atom.id
                        coord=atom.get_coord()

                        (a1,b1,c1)=all_random(0.5,0.1)
                        Atom.set_coord(protein_structure[a][b][c][e], np.array([coord[0]+a1, coord[1]+b1, coord[2]+c1]))
                        if coord[0]+a1<-500 or  coord[1]+b1<-500 or coord[2]+c1<-500:
                            print([coord[0]+a1, coord[1]+b1, coord[2]+c1])
                        count=count+1
                ij=ij+1

    return protein_structure


def all_random(chance, value_range):
    p = random.random()
    a=0
    b=0
    c=0
    if p < chance:
        p = random.random()
        value = ((p-.5)*2) * value_range
        p = random.random()
        if p < 0.3333333:
            a = value
        elif p < 0.66666666:
            b = value
        else:
            c = value
    return (a,b,c)

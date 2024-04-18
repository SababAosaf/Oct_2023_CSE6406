import math


import random

import numpy as np
from Bio.PDB import Superimposer
from Bio.PDB.Atom import Atom
from deap.tools import cxSimulatedBinary

import copy
def protein_stat(protein_structure_1, protein_structure_2):
    protein_structure_2=superimpose_proteins(protein_structure_1,protein_structure_2)
    protein_structure_1_atoms=get_atoms(protein_structure_1)
    protein_structure_2_atoms = get_atoms(protein_structure_2)

    protein_structure_1_coord=[]
    protein_structure_2_coord = []

    for model in protein_structure_1:
        a=model.id
        for chain in model:
            b=chain.id
            for residue in chain:
                c=residue.id
                for atom in residue:
                    e=atom.id
                    coord=atom.get_coord()
                    protein_structure_1_coord.append((residue.get_resname(),atom.id,atom.get_coord()))
    for model in protein_structure_2:
        a=model.id
        for chain in model:
            b=chain.id
            for residue in chain:
                c=residue.get_resname()

                for atom in residue:
                    e=atom.id

                    protein_structure_2_coord.append((residue.get_resname(),atom.id,atom.get_coord()))




    values=[]
    for i in range(0, len(protein_structure_2_coord)):
        sp=protein_structure_1_coord[i][2][0]-protein_structure_2_coord[i][2][0]
        sg=protein_structure_1_coord[i][2][1]-protein_structure_2_coord[i][2][1]
        sf=protein_structure_1_coord[i][2][2]-protein_structure_2_coord[i][2][2]
        s=sp**2+sg**2+sf**2
        s=math.sqrt(s)
        values.append((protein_structure_1_coord[i][0],protein_structure_1_coord[i][1],s))

    return values



def crossover(protein_structure_1, protein_structure_2):
    protein_structure_2=superimpose_proteins(protein_structure_1,protein_structure_2)
    protein_structure_1_atoms=get_atoms(protein_structure_1)
    protein_structure_2_atoms = get_atoms(protein_structure_2)

    protein_structure_1_coord=[]
    protein_structure_2_coord = []
    for atom in protein_structure_1_atoms:
        coord=atom.get_coord()

        protein_structure_1_coord.append(coord[0])
        protein_structure_1_coord.append(coord[1])
        protein_structure_1_coord.append(coord[2])

    for atom in protein_structure_2_atoms:
        coord=atom.get_coord()
        protein_structure_2_coord.append(coord[0])
        protein_structure_2_coord.append(coord[1])
        protein_structure_2_coord.append(coord[2])


    (protein_structure_1_coord_child,protein_structure_2_coord_child)=cxSimulatedBinary(copy.deepcopy(protein_structure_1_coord),copy.deepcopy(protein_structure_2_coord),0.01)


    count=0
    for model in protein_structure_1:
        a=model.id
        for chain in model:
            b=chain.id
            for residue in chain:
                c=residue.id
                for atom in residue:
                    e=atom.id
                    Atom.set_coord(protein_structure_1[a][b][c][e], np.array([protein_structure_1_coord_child[count], protein_structure_1_coord_child[count+1], protein_structure_1_coord_child[count+2]]))
                    count=count+3
    count=0
    for model in protein_structure_2:
        a=model.id
        for chain in model:
            b=chain.id
            for residue in chain:
                c=residue.id
                for atom in residue:
                    e=atom.id
                    Atom.set_coord(protein_structure_2[a][b][c][e], np.array([protein_structure_2_coord_child[count], protein_structure_2_coord_child[count+1], protein_structure_2_coord_child[count+2]]))
                    count=count+3



    return (protein_structure_1,protein_structure_2)


def cxSimulatedBinary(ind1, ind2, eta):
    """Executes a simulated binary crossover that modify in-place the input
    individuals. The simulated binary crossover expects :term:`sequence`
    individuals of floating point numbers.

    :param ind1: The first individual participating in the crossover.
    :param ind2: The second individual participating in the crossover.
    :param eta: Crowding degree of the crossover. A high eta will produce
                children resembling to their parents, while a small eta will
                produce solutions much more different.
    :returns: A tuple of two individuals.

    This function uses the :func:`~random.random` function from the python base
    :mod:`random` module.
    """
    for i, (x1, x2) in enumerate(zip(ind1, ind2)):
        rand = random.random()
        if rand <= 0.5:
            beta = 2. * rand
        else:
            beta = 1. / (2. * (1. - rand))

        beta **= 1. / (eta + 1.)

        ind1[i] = 0.5 * (((1 + beta) * x1) + ((1 - beta) * x2))

        ind2[i] = 0.5 * (((1 - beta) * x1) + ((1 + beta) * x2))

    return ind1, ind2





def get_atoms(structure):
    atoms=[]
    for model in structure:
        for chain in model:
            for residue in chain:
                for atom in residue:
                    atoms.append(atom)
    return atoms

def superimpose_proteins(protein_structure_1,protein_structure_2):
    protein_structure_1_atoms = get_atoms(protein_structure_1)
    protein_structure_2_atoms = get_atoms(protein_structure_2)
    sup = Superimposer()
    sup.set_atoms(protein_structure_1_atoms,protein_structure_2_atoms)
    sup.apply(protein_structure_2_atoms)



    atom_serial=0
    for model in protein_structure_2:
        a=model.id
        for chain in model:
            b=chain.id
            for residue in chain:
                c=residue.id
                for atom in residue:
                    e=atom.id
                    coord = protein_structure_2_atoms[atom_serial].get_coord()
                    atom_serial=atom_serial+1
                    Atom.set_coord(protein_structure_2[a][b][c][e], (coord[0] , coord[1] , coord[2] ))
    return  protein_structure_2






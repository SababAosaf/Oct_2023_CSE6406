import math
import pickle
import random
from Bio.PDB import PDBParser, PDBIO
from pymoo.core.sampling import Sampling
import numpy as np
import Bio.PDB
import MyProblem
import cheks12
import contactMap
import stat_generator
import stats
from initialize_targets import intialize_targets_folder


class MySampling(Sampling):

    def _do(self, problem , n_samples, **kwargs):

        d3to1 = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
         'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N',
         'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
         'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}

        stat_path=problem.stat_path
        contacts_path=problem.contact_path
        print("<<")
        problem.contact=contactMap.generateContactMap(contacts_path)
        print(problem.contact)
        print(">>")
        structure = Bio.PDB.PDBParser().get_structure('Structure',contacts_path)
        s=''
        for model in structure:
         for chain in model:
             seq = []
             for residue in chain:
                 seq.append(d3to1[residue.resname])
             s=''.join(seq)
        problem.native_sequence=s
        initialization_path=problem.init_path

        stat_generator.generate_stats(stat_path,'relaxed_model_',5,1,'','_pred_0.pdb')
        allow=stats.freq("Current_Stats\\total.csv")
        allow=allow[:10]
        allows=[]
        for ijk in allow:
            allows.append(ijk[0])

        problem.allows=allows
        proteins=intialize_targets_folder(initialization_path,allows,"relaxed_model_(.*)_pred_0.pdb",n_samples)
        X = np.full((n_samples, 1), 0,dtype=object)


        for i in range(n_samples):
            X[i, 0] = proteins[i]

        return X

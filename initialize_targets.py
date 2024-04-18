import json
import os
import re

from Bio.PDB import PDBParser, PDBIO

import protein_mutation



def intialize_targets_folder(folder,allows,protein_reg,protein_count):

    print("CALLING intialize_targets_folder")
    files=os.listdir(folder)
    proteins=[]
    parser = PDBParser()
    counts=int(protein_count/5)
    for i in files:

        pattern = re.compile(protein_reg)
        print(protein_reg)
        if not pattern.match(i):
            continue
        # print("THE FILE:"+i)
        file=folder+"\\"+i
        print(file)

        structure = parser.get_structure('PH',file)
        proteins.append(structure)



        for j in range(0,counts):
            structure2=protein_mutation.mutate1(structure,allows)
            proteins.append(structure2)

    return proteins




def intialize_targets(protein_id,parser,allows):

    try:
        teams=open('D:\Projects\protein_metaheuristics\casp14\\'+protein_id+'.txt')
    except:
        teams=open('D:\Projects\protein_metaheuristics\casp14\\'+protein_id+'-D1.txt')

    team_collection=[]
    theTeams=''
    for i in teams.readlines():
        try:
            while '  ' in i:
                i=i.replace('  ', ' ')

            j=i.split(' ')

            team=j[1]


            if len(team)>5:
                team_collection.append(team)


        except:
            pass


    teams55=team_collection[len(team_collection)-5:len(team_collection)]
    teams55.extend(team_collection[0:5])
    print(teams55)
    teams555=''
    for i in teams55:
        teams555=teams555+','+i
    print(teams555)

    folder='D:\\Projects\\protein_metaheuristics\\population\\'+protein_id+'\\all_teams'
    files=os.listdir(folder)
    #os.mkdir("D:\\Projects\\protein_metaheuristics\\population\\"+protein_id+"\\generation_1\\")


    for i in files:
        print(i)
        if i in teams555:
            file=folder+"\\"+i
            print(file)
            io = PDBIO()
            structure = parser.get_structure('PH',file)
            io.set_structure(structure)
            io.save("D:\\Projects\\protein_metaheuristics\\population\\"+protein_id+"\\generation_1\\"+i)

            for j in range(0,9):
                structure2=protein_mutation.mutate1(structure,allows)
                io.set_structure(structure2)
                io.save("D:\\Projects\\protein_metaheuristics\\population\\"+protein_id+"\\generation_1\\"+str(j)+"_" + i)


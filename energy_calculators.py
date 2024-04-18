import os
import shutil



def energy(pdb):

    enegry_calculator_directory = 'D:\\Projects\\Msc_Research\\Protein_Folding\\protein_metaheuristics\\energy_calculator'
    shutil.copyfile(pdb, enegry_calculator_directory + '\\current' + '.pdb')
    command = enegry_calculator_directory + "\\foldx.exe  --command=Stability --pdb=current"  + ".pdb"
    #print("<fold>")
    os.chdir(enegry_calculator_directory)
    energy = os.popen(command).read()
    print(command)
    e=''
    energy_names=''
    for line in energy.splitlines():
        if '=' in line:

            energies=line.split('=')
            energy_type=energies[0].strip()
            try:
                energy_value=energies[1].strip()
            except :
                energy_value='0'
            energy_names=energy_names+','+energy_type
            e=e+','+energy_value
    e=e[1:]

    energy_names=energy_names[1:]
    os.remove(enegry_calculator_directory + '\\current'  + '.pdb')
    return (energy_names,e)



#energy('D:\\Projects\\Msc_Research\\Protein_Folding\\protein_metaheuristics\\population\\T1024\\all_teams\\T1024TS032_1')
targets = os.listdir('D:\Projects\protein_metaheuristics\\targets')
for i in targets:

    try:
        id= i[0:i.index('.')]
        protein_team_file='D:\\Projects\\protein_metaheuristics\\casp14\\'+id+'.txt'

        try:
            try:
                f=open(protein_team_file,'r')
            except:
                protein_team_file = 'D:\\Projects\\protein_metaheuristics\\casp14\\' + id + '-D1.txt'
                f = open(protein_team_file, 'r')
        except:
            continue
        count = 0
        teams_value = []
        for j in f.readlines():
            count = count + 1
            if count > 2 and len(j) > 20:
                pass

                list_ = j.split()
                teams_1 = list_[1]
                if '-D1' in teams_1:
                    teams_1 = teams_1[:teams_1.index('-D1')]
                teams_value.append(teams_1)
        first_line=''
        files=''
        teams_value=teams_value[0:3]
        dict={'team_id':[]}
        lines=[]

        for team_id in teams_value:
            teams = 'D:\Projects\protein_metaheuristics\population\\' + id + '\\all_teams\\'+team_id
            energies55=energy(teams)
            energy_names=energies55[0].split(',')
            for ikj in energy_names:
                if ikj not in dict.keys():
                    dict[ikj]=[]

            dict['team_id'].append(team_id)
            energy_values=energies55[1].split(',')
            dc=0
            for ikj in energy_values:
                dict[energy_names[dc]].append(ikj)
                dc=dc+1
            #first_line='team_id,'+energies55[0]
            #lines55=team_id+','+energies55[1]
            #files=files+'\n'+lines55
            #print(lines55)
        print(dict)

        for key in dict:
            if lines is []:
                lines=lines.append(key)
            else:
                lines[0]=lines[0]+','+key
            p=1
            # for j in dict[key]:
            #     if line[p]
            #
            # print(key, '->', a_dict[key])
        files=first_line+files

        open('D:\\Projects\\Msc_Research\\Protein_Folding\\energy\\'+i+'.csv','w').write(files)
    except:
        pass


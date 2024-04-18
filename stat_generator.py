import os
import traceback
from operator import itemgetter

import protein_operators
from Bio.PDB import PDBParser, PDBIO
parser = PDBParser()
def generate___():
    targets = os.listdir('D:\Projects\protein_metaheuristics\\targets')
    print(55)

    counts=1
    for_embed=[]
    sequence_size=50
    big_sec = []
    s_sec=[]
    seq=[]
    filez=open('files','w')
    filez_ = open('p', 'w')
    filez__ = open('n', 'w')
    file123=open('list55','w')
    prtein_specific_list=[]

    ############## CHOOSING A SPECIFIC PROTEIN #############################
    for i in targets:#[0:1]:
        print(i)
        pdb_name=i
        serials=[]
        current_protein=i
        seq5=[]
        prtein_specific_list=[]
        print(
        )
        print()


        counts=counts+1
        if counts<=28:
            continue

        print(i)
        lists15=[]

        for i565 in range(0,10):
            lists15.append(i565)
        ########### PROTEIN PAIRS (TEAMS) FOR COMPARISON
        protein_pair= [(a, b) for idx, a in enumerate(lists15) for b in lists15[idx + 1:]]
        ########### WE HAVE ALL PAIRS FOR COMPARISON. AND NOW COMPARISON




        ###### <ALL PAIR COMPARISON LOOP>
        for ip in protein_pair:
            try:

                seq5=[]
                print(i)
                id = pdb_name[0:pdb_name.index('.')]
                teams = 'D:\Projects\protein_metaheuristics\population\\' + id + '\\all_teams'

                if os.path.exists(teams):
                    pass
                else:
                    teams = 'D:\Projects\protein_metaheuristics\population\\' + id + '_Check\\all_teams'

                ranking_folder = 'D:\Projects\protein_metaheuristics\casp14\\'

                if os.path.isfile(ranking_folder + id + '.txt'):
                    comparison_file = open(ranking_folder + id + '.txt')
                else:
                    comparison_file = open(ranking_folder + id + '-D1.txt')

                count = 0
                teams_value = []
                for j in comparison_file.readlines():
                    count = count + 1
                    if count > 2 and len(j) > 20:
                        pass

                        print('<LINE>' + j + '</LINE>')
                        list_ = j.split()
                        teams_1 = list_[1]
                        if '-D1' in teams_1:
                            teams_1 = teams_1[:teams_1.index('-D1')]
                        teams_value.append(teams_1)

                print(teams_value)

                best_protein = teams_value[ip[0]]
                pt=[]

                pt.append(ip[1])

                count = 0
                best_proteins = teams + '\\' + best_protein

                protein_structure_1=parser.get_structure('P5', best_proteins + '')
                listr=[]

                atop_pos=0
                rpos=0
                dict_={}
                for model in protein_structure_1:
                    a = model.id
                    for chain in model:
                        b = chain.id
                        for residue in chain:
                            c = residue.id
                            listr.append([residue.get_resname(),[]])

                            for atom in residue:
                                e = atom.id
                                coord = atom.get_coord()
                                residue.get_resname()
                                dict_[atop_pos]=rpos
                                atop_pos=atop_pos+1
                            rpos=rpos+1



                for jg in pt:
                    j=teams_value[jg]

                    count = count + 1
                    comparator_protein = teams + '\\' + j
                    best_proteins = teams + '\\' + best_protein

                    # positions=protein_operators.protein_stat(parser.get_structure('P1',standard+'.pdb'),parser.get_structure('P2',comparator_protein))
                    positions = protein_operators.protein_stat(parser.get_structure('P1', best_proteins + ''),
                                                       parser.get_structure('P2', comparator_protein))

                    position_=0
                    for item in positions:

                        listr[dict_[position_]][1].append(item[2])
                        position_=position_+1



                print(listr)
                positions=0
                pr=listr
                print(listr)
                for i in listr:
                    pj=len(i[1])
                    s=0
                    for j in i[1]:
                        s=s+j
                    s=s/pj
                    pr[positions][1]=s
                    positions=positions+1
                print(pr)
                print(len(pr))
                fline=''
                dline=''
                for i in pr:
                    fline=fline+','+ i[0]
                    dline=dline+','+str(i[1])
                fline=fline[1:]
                dline=dline[1:]
                fline=fline+'\n'+dline
                files1=open(current_protein+'r_seq.csv','w')
                files1.write(fline)

                current_value=0
                print(len(seq))

                for i551 in range(len(pr)-sequence_size):
                    current_sequence=''
                    for j in range(i551,i551+sequence_size):
                        current_sequence=current_sequence+' '+pr[j][0]
                        current_value=current_value+pr[j][1]
                    current_sequence=current_sequence[1:]
                    #print(current_sequence)
                    current_value=current_value/sequence_size


                    seq.append((current_sequence,current_value))
                    if i551 % sequence_size==0 or True:
                        seq5.append((current_sequence, current_value))

                print(len(seq5))

                seq2 = []
                i123 = 1
                for ikj in seq5:
                    seq2.append(((ikj[0], i123), ikj[1]))
                    i123 = i123 + 1
                prtein_specific_list=seq5
                seq2=sorted(seq2,key=itemgetter(1))
                sp=[]
                for ijh in seq2:
                    sp.append(ijh[0][1])
                print(sp)
                serials.append(sp)

                for i551 in range(0, len(seq)):
                    for_embed.append(seq[i551])

            except Exception as e:
                traceback.print_exc()

        ####              </ALL PAIR COMPARISON LOOP>



        print(serials)
        dict_rank={}
        for i in range(1,len(serials[0])+1):
            dict_rank[i]=0
        for j in serials:
            dict_rank[j[0]]=dict_rank[j[0]]+1
        print(dict_rank)
        list5555 = [(k, v) for k, v in dict_rank.items()]
        list5555=sorted(list5555,key=itemgetter(1),reverse=True)
        lg=[]


        lg.append(list5555[0])


        print(prtein_specific_list)
        print(list5555)


        for ijk  in lg:

            file123.write(prtein_specific_list[ijk[0]-1][0] + '\n')
            '''
            if i4454[0][1] in lg:
                print(i4454[0][0] + '\n')'''
            #file123.write(seq5[ijk[0]][0] + '\n')


def generate__():
    targets = os.listdir('D:\Projects\protein_metaheuristics\\targets')

    counts=1
    for_embed=[]
    sequence_size=50
    big_sec = []
    s_sec=[]
    seq=[]
    filez=open('files','w')
    filez_ = open('p', 'w')
    filez__ = open('n', 'w')

    for i in targets:
        current_protein=i



        counts=counts+1
        if counts>28:
            continue

        print(i)
        try:
            id = i[0:i.index('.')]
            teams = 'D:\Projects\protein_metaheuristics\population\\' + id + '\\all_teams'

            if os.path.exists(teams):
                team_results = os.listdir(teams)
            else:
                team_results = os.listdir('D:\Projects\protein_metaheuristics\population\\' + id + '_Check\\all_teams')
                teams = 'D:\Projects\protein_metaheuristics\population\\' + id + '_Check\\all_teams'
            standard = 'D:\Projects\protein_metaheuristics\\targets\\' + id
            ranking_folder = 'D:\Projects\protein_metaheuristics\casp14\\'

            if os.path.isfile(ranking_folder + id + '.txt'):
                comparison_file = open(ranking_folder + id + '.txt')
            else:
                comparison_file = open(ranking_folder + id + '-D1.txt')

            count = 0
            teams_value = []
            for j in comparison_file.readlines():
                count = count + 1
                if count > 2 and len(j) > 20:
                    pass

                    print('<LINE>' + j + '</LINE>')
                    list_ = j.split()
                    teams_1 = list_[1]
                    if '-D1' in teams_1:
                        teams_1 = teams_1[:teams_1.index('-D1')]
                    teams_value.append(teams_1)

            print(teams_value)
            best_protein = teams_value[0]
            count = 0
            file = ''
            rline = ''
            aline = ''
            pline = ''
            dictr={}
            best_proteins = teams + '\\' + best_protein
            protein_structure_1=parser.get_structure('P5', best_proteins + '')
            listr=[]

            atop_pos=0
            rpos=0
            dict_={}
            for model in protein_structure_1:
                a = model.id
                for chain in model:
                    b = chain.id
                    for residue in chain:
                        c = residue.id
                        listr.append([residue.get_resname(),[]])

                        for atom in residue:
                            e = atom.id
                            coord = atom.get_coord()
                            residue.get_resname()
                            dict_[atop_pos]=rpos
                            atop_pos=atop_pos+1
                        rpos=rpos+1



            for j in teams_value[1:10]:
                try:
                    count = count + 1
                    comparator_protein = teams + '\\' + j
                    best_proteins = teams + '\\' + best_protein

                    # positions=protein_operators.protein_stat(parser.get_structure('P1',standard+'.pdb'),parser.get_structure('P2',comparator_protein))
                    positions = protein_operators.protein_stat(parser.get_structure('P1', best_proteins + ''),
                                                       parser.get_structure('P2', comparator_protein))
                    pline = ''


                    p_item='CP'
                    lists=[]
                    position_=0
                    for item in positions:

                        listr[dict_[position_]][1].append(item[2])
                        position_=position_+1





                        '''if item[1] == 'CA' or item[1] == 'C' or item[1] == 'N':
                            if count == 1:
                                rline = rline + ',' + item[0]
                                aline = aline + ',' + item[1]
                            pline = pline + ',' + str(item[2])
                    print(positions)
                    if count == 1:
                        file = rline[1:] + '\n' + aline[1:] + '\n'
                    file = file + '\n' + pline[1:]'''



                except Exception as e:
                    pass

            print(listr)
            positions=0
            pr=listr

            for i in listr:
                pj=len(i[1])
                s=0
                for j in i[1]:
                    s=s+j
                s=s/pj
                pr[positions][1]=s
                positions=positions+1
            print(pr)
            fline=''
            dline=''
            for i in pr:
                fline=fline+','+ i[0]
                dline=dline+','+str(i[1])
            fline=fline[1:]
            dline=dline[1:]
            fline=fline+'\n'+dline
            print(fline)
            print(dline)
            files1=open(current_protein+'r_seq.csv','w')
            files1.write(fline)




            current_sequence=""
            current_value=0
            for i in range(len(pr)-sequence_size):
                current_sequence=''
                for j in range(i,i+sequence_size):
                    current_sequence=current_sequence+' '+pr[j][0]
                    current_value=current_value+pr[j][1]
                current_sequence=current_sequence[1:]
                #print(current_sequence)
                current_value=current_value/sequence_size


                seq.append((current_sequence,current_value))


            for i in range(0, len(seq)):
                for_embed.append(seq[i])
        except Exception as e:
            traceback.print_exc()

    l5= len(seq)
    pk=l5/5
    seq=sorted(seq,key=itemgetter(1))
    for i in range(0, int(pk)):
        big_sec.append(seq[i])
    seq=sorted(seq,key=itemgetter(1),reverse=True)
    for i in range(0, int(pk)):
        s_sec.append(seq[i])


    for i in big_sec:
        filez__.write(i[0])
        filez__.write('\n')
    for i in s_sec:
        filez_.write(i[0])
        filez_.write('\n')
    for i in for_embed:
        filez.write(i[0])
        filez.write('\n')


    print(s_sec)
def generate_():
    targets = os.listdir('D:\Projects\protein_metaheuristics\\targets')

    counts=1
    for_embed=[]
    sequence_size=2
    big_sec = []
    s_sec=[]
    filez=open('files','w')
    filez_ = open('p', 'w')
    filez__ = open('n', 'w')

    for i in targets:


        seq = []

        counts=counts+1
        if counts>28:
            continue

        print(i)
        try:
            id = i[0:i.index('.')]
            teams = 'D:\Projects\protein_metaheuristics\population\\' + id + '\\all_teams'

            if os.path.exists(teams):
                team_results = os.listdir(teams)
            else:
                team_results = os.listdir('D:\Projects\protein_metaheuristics\population\\' + id + '_Check\\all_teams')
                teams = 'D:\Projects\protein_metaheuristics\population\\' + id + '_Check\\all_teams'
            standard = 'D:\Projects\protein_metaheuristics\\targets\\' + id
            ranking_folder = 'D:\Projects\protein_metaheuristics\casp14\\'

            if os.path.isfile(ranking_folder + id + '.txt'):
                comparison_file = open(ranking_folder + id + '.txt')
            else:
                comparison_file = open(ranking_folder + id + '-D1.txt')

            count = 0
            teams_value = []
            for j in comparison_file.readlines():
                count = count + 1
                if count > 2 and len(j) > 20:
                    pass

                    print('<LINE>' + j + '</LINE>')
                    list_ = j.split()
                    teams_1 = list_[1]
                    if '-D1' in teams_1:
                        teams_1 = teams_1[:teams_1.index('-D1')]
                    teams_value.append(teams_1)

            print(teams_value)
            best_protein = teams_value[0]
            count = 0
            file = ''
            rline = ''
            aline = ''
            pline = ''
            dictr={}
            best_proteins = teams + '\\' + best_protein
            protein_structure_1=parser.get_structure('P5', best_proteins + '')
            listr=[]

            atop_pos=0
            rpos=0
            dict_={}
            for model in protein_structure_1:
                a = model.id
                for chain in model:
                    b = chain.id
                    for residue in chain:
                        c = residue.id
                        listr.append([residue.get_resname(),[]])

                        for atom in residue:
                            e = atom.id
                            coord = atom.get_coord()
                            residue.get_resname()
                            dict_[atop_pos]=rpos
                            atop_pos=atop_pos+1
                        rpos=rpos+1



            for j in teams_value[1:10]:
                try:
                    count = count + 1
                    comparator_protein = teams + '\\' + j
                    best_proteins = teams + '\\' + best_protein

                    # positions=protein_operators.protein_stat(parser.get_structure('P1',standard+'.pdb'),parser.get_structure('P2',comparator_protein))
                    positions = protein_operators.protein_stat(parser.get_structure('P1', best_proteins + ''),
                                                       parser.get_structure('P2', comparator_protein))
                    pline = ''


                    p_item='CP'
                    lists=[]
                    position_=0
                    for item in positions:

                        listr[dict_[position_]][1].append(item[2])
                        position_=position_+1





                        '''if item[1] == 'CA' or item[1] == 'C' or item[1] == 'N':
                            if count == 1:
                                rline = rline + ',' + item[0]
                                aline = aline + ',' + item[1]
                            pline = pline + ',' + str(item[2])
                    print(positions)
                    if count == 1:
                        file = rline[1:] + '\n' + aline[1:] + '\n'
                    file = file + '\n' + pline[1:]'''



                except Exception as e:
                    pass

            #print(listr)
            positions=0
            pr=listr

            for i in listr:
                pj=len(i[1])
                s=0
                for j in i[1]:
                    s=s+j
                s=s/pj
                pr[positions][1]=s
                positions=positions+1
            #print(pr)

            current_sequence=""
            current_value=0
            for i in range(len(pr)-sequence_size):
                current_sequence=''
                for j in range(i,i+sequence_size):
                    current_sequence=current_sequence+' '+pr[j][0]
                    current_value=current_value+pr[j][1]
                current_sequence=current_sequence[1:]
                #print(current_sequence)
                current_value=current_value/sequence_size


                seq.append((current_sequence,current_value))
            print(seq)

            seq=sorted(seq, key=itemgetter(1))

            for i in range(0,5):
                big_sec.append(seq[i])
            seq = sorted(seq, key=itemgetter(1),reverse=True)
            for i in range(0,5):
                s_sec.append(seq[i])
            for i in range(0, len(seq)):
                for_embed.append(seq[i])
        except Exception as e:
            traceback.print_exc()
    print(big_sec)

    for i in big_sec:
        filez__.write(i[0])
        filez__.write('\n')
    for i in s_sec:
        filez_.write(i[0])
        filez_.write('\n')
    for i in for_embed:
        filez.write(i[0])
        filez.write('\n')


    print(s_sec)


# PREDICTION PIPELINE
def generate():
    targets=os.listdir('D:\Projects\protein_metaheuristics\\targets')
    #targets=['T1025.pdb']
    for i in targets:
        print(i)
        try:
            id=i[0:i.index('.')]
            teams='D:\Projects\protein_metaheuristics\population\\'+id+'\\all_teams'


            if os.path.exists(teams):
                team_results=os.listdir(teams)
            else:
                team_results=os.listdir('D:\Projects\protein_metaheuristics\population\\'+id+'_Check\\all_teams')
                teams='D:\Projects\protein_metaheuristics\population\\'+id+'_Check\\all_teams'
            standard='D:\Projects\protein_metaheuristics\\targets\\'+id
            ranking_folder='D:\Projects\protein_metaheuristics\casp14\\'

            if os.path.isfile(ranking_folder+id+'.txt'):
                comparison_file=open(ranking_folder+id+'.txt')
            else:
                comparison_file=open(ranking_folder+id+'-D1.txt')

            count=0
            teams_value=[]
            for j in comparison_file.readlines():
                count=count+1
                if count>2 and len(j)>20:
                    pass

                    print('<LINE>'+j+'</LINE>')
                    list_=j.split()
                    teams_1= list_[1]
                    if '-D1' in teams_1:
                        teams_1=teams_1[:teams_1.index('-D1')]
                    teams_value.append(teams_1)

            print(teams_value)
            best_protein=teams_value[0]
            count=0
            file=''
            rline=''
            aline=''
            pline=''
            for j in teams_value[1:]:
                try:
                    count=count+1
                    comparator_protein= teams+'\\'+j
                    best_proteins= teams+'\\'+best_protein

                    #positions=protein_operators.protein_stat(parser.get_structure('P1',standard+'.pdb'),parser.get_structure('P2',comparator_protein))
                    positions=protein_operators.protein_stat(parser.get_structure('P1',best_proteins+''),parser.get_structure('P2',comparator_protein))
                    pline=''
                    for item in positions:
                        if item[1]=='CA' or item[1]=='C' or item[1]=='N':
                            if count==1:
                                rline=rline+','+item[0]
                                aline=aline+','+item[1]
                            pline=pline+','+str(item[2])
                    print(positions)
                    if count==1:
                        file=rline[1:]+'\n'+aline[1:]+'\n'
                    file=file+'\n'+pline[1:]
                except Exception as e:
                    pass
            f=open(id+'_total.csv','w')
            f.write(file)
        except Exception as e:
            traceback.print_exc()
def generate_stats(folder_of_protein_sequences,protein_name_starts,sequence_count,sequence_start,folder_name_starts, sequence_name_more):
    targets=os.listdir(folder_of_protein_sequences)
    print("generate_stats()")
    print(folder_of_protein_sequences)
    #targets=['T1025.pdb']
    folder_of_protein_sequences_=folder_of_protein_sequences[0:folder_of_protein_sequences.rfind('\\')]
    targets=[folder_of_protein_sequences[folder_of_protein_sequences.rfind('\\')+1:len(folder_of_protein_sequences)]
    ]
    folder_of_protein_sequences=folder_of_protein_sequences_
    for i in targets:
        print("LINE 1: "+i)
        if not folder_name_starts in i:
            continue
        print()
        print(i)
        try:


            count=0
            file=''
            rline=''
            aline=''
            pline=''

            for j in range(sequence_start,sequence_count+sequence_start):
                try:

                    print('HERE')
                    comparator_protein=folder_of_protein_sequences+'\\'+str(i)+'\\'+protein_name_starts+str(j)+sequence_name_more
                    best_proteins= folder_of_protein_sequences+'\\'+str(i)+'\\'+protein_name_starts+str(sequence_start)+sequence_name_more
                    print('HER55E')
                    print(best_proteins)
                    print('best_protein'+best_proteins)
                    print(comparator_protein)

                    if comparator_protein==best_proteins:
                        continue
                    count=count+1
                    print(count)
                    #positions=protein_operators.protein_stat(parser.get_structure('P1',standard+'.pdb'),parser.get_structure('P2',comparator_protein))
                    positions=protein_operators.protein_stat(parser.get_structure('P1',best_proteins+''),parser.get_structure('P2',comparator_protein))
                    pline=''
                    for item in positions:
                        if item[1]=='CA' or item[1]=='C' or item[1]=='N':
                            if count==1:
                                rline=rline+','+item[0]
                                aline=aline+','+item[1]
                            pline=pline+','+str(item[2])
                    print(positions)
                    if count==1:
                        file=rline[1:]+'\n'+aline[1:]+'\n'
                    file=file+'\n'+pline[1:]
                except Exception as e:
                    traceback.print_exc()
                    pass
            f=open("Current_Stats"+'\\total.csv','w')
            print(folder_of_protein_sequences+'\\'+i+'\\'+i+'_total.csv')
            f.write(file)
            print(file)
            f.close()
        except Exception as e:
            print("555")
            traceback.print_exc()

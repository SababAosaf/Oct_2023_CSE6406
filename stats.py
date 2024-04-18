import os
import csv

def freq_____():
    files = os.listdir('D:\Projects\Msc_Research\Protein_Folding\protein_metaheuristics_code')
    m = 0

    #files = ['T1035_total.csv']
    for i in files:
        #print(i)
        if 'l.csv' in i:
            #print(i)
            with open(i) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                mm = 0
                dict = {}
                atom = []
                rd = []
                r_positions={}
                dictposavg={}
                for row in csv_reader:
                    #print(len(row))
                    mm = 0
                    m = 0

                    if line_count == 0:
                        line_count += 1
                        rd = row
                        pos=1
                        for ijkp in rd:
                            r_positions[ijkp]=[]
                            dictposavg[pos]=0
                            pos=pos+1
                        #print(r_positions)
                    elif line_count == 1:
                        line_count += 1
                        atom = row
                    elif line_count == 2:
                        line_count += 1
                    else:
                        serial = -1

                        best = 1
                        i = 0

                        for ij in row:

                            serial = serial + 1
                            if serial not in dict:
                                dict[serial] = 0
                            if i - 2 > -1:
                                a = row[i - 2]
                            else:
                                a = 0

                            if i - 1 > -1:
                                b = row[i - 1]
                            else:
                                b = 0

                            if i + 1 < len(row):
                                c = row[i + 1]
                            else:
                                c = 0

                            if i + 2 < len(row):
                                d = row[i + 2]
                            else:
                                d = 0

                            val5=ij
                            ij = (float(a) + float(b) + float(ij) + float(c) + float(d)) / 5
                            if float(ij) > mm:
                                mm = float(ij)
                                best = serial
                            r_positions[rd[serial-1]].append(ij)

                            i = i + 1
                            dictposavg[i]=dictposavg[i]+float(val5)

                        dict[best] = dict[best] + 1

                        line_count += 1
                sorted_footballers_by_goals = sorted(dict.items(), key=lambda x: x[1], reverse=True)
                #print(sorted_footballers_by_goals)
                #print(len(sorted_footballers_by_goals))
                top_10 = sorted_footballers_by_goals
                strings = []
                rg = []
                r_pos = {}

                for i55 in top_10:
                    i = i55[0]
                    ul = 0
                    tl = len(rd)
                    if i - 5 > 0:
                        ul = i - 5
                    if i + 5 < len(rd):
                        tl = i + 5

                    rds = ''
                    rs = ''
                    for ijk in range(ul, tl):
                        rs = rs + atom[ijk]

                    strings.append(rs)
                    rg.append(rd[i])

                #for ij in strings:
                    #print(ij)
                #for ij in rg:
                    #print(ij)
                avg={}
                for r in r_positions.items():
                    avg1=sum(r[1])/len(r[1])
                    avg[r[0]]=avg1
                sorted_footballers_by_goals = sorted(avg.items(), key=lambda x: x[1], reverse=True)
                # print(sorted_footballers_by_goals)
                # print(dictposavg)

                sorted_footballers_by_goals = sorted(dictposavg.items(), key=lambda x: x[1],reverse=False)
                #print(sorted_footballers_by_goals)
                #print(f'Processed {line_count} lines.')
                list_check=[]
                for i in sorted_footballers_by_goals:
                    flag=5
                    for j in list_check:
                        if abs(i[0]-j)<10:
                            flag=7
                    if flag==7:
                        continue

                    cur=i[0]-1
                    ul = 0
                    tl = len(rd)-1
                    if i[0]-1 - 5 > 0:
                        ul = i[0]-1 - 5
                    if i[0]-1 + 5 < len(rd)-1:
                        tl = i[0] -1+ 5
                    for jk in range(ul,tl):
                        print(rd[jk] , end=' ')
                    print()
                    list_check.append(i[0])
def freq____():
    files = os.listdir('D:\Projects\Msc_Research\Protein_Folding\protein_metaheuristics_code')
    m = 0
    files = ['T1033_total.csv']
    for i in files:
        print(i)
        if 'csv' in i:
            print(i)
            with open(i) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                mm = 0
                dict = {}
                atom = []
                rd = []
                r_positions={}
                for row in csv_reader:
                    print(len(row))
                    mm = 0
                    m = 0

                    if line_count == 0:
                        line_count += 1
                        rd = row
                        for ijkp in rd:
                            r_positions[ijkp]=[]
                        print(r_positions)
                    elif line_count == 1:
                        line_count += 1
                        atom = row
                    elif line_count == 2:
                        line_count += 1
                    else:
                        serial = -1

                        best = 1
                        i = 0

                        for ij in row:

                            serial = serial + 1
                            if serial not in dict:
                                dict[serial] = 0
                            if i - 2 > -1:
                                a = row[i - 2]
                            else:
                                a = 0

                            if i - 1 > -1:
                                b = row[i - 1]
                            else:
                                b = 0

                            if i + 1 < len(row):
                                c = row[i + 1]
                            else:
                                c = 0

                            if i + 2 < len(row):
                                d = row[i + 2]
                            else:
                                d = 0

                            ij = (float(a) + float(b) + float(ij) + float(c) + float(d)) / 5
                            if float(ij) > mm:
                                mm = float(ij)
                                best = serial
                            r_positions[rd[serial-1]].append(ij)

                            i = i + 1

                        dict[best] = dict[best] + 1

                        line_count += 1
                sorted_footballers_by_goals = sorted(dict.items(), key=lambda x: x[1], reverse=True)
                print(sorted_footballers_by_goals)
                print(len(sorted_footballers_by_goals))
                top_10 = sorted_footballers_by_goals
                strings = []
                rg = []
                r_pos = {}

                for i55 in top_10:
                    i = i55[0]
                    ul = 0
                    tl = len(rd)
                    if i - 5 > 0:
                        ul = i - 5
                    if i + 5 < len(rd):
                        tl = i + 5

                    rds = ''
                    rs = ''
                    for ijk in range(ul, tl):
                        rs = rs + atom[ijk]

                    strings.append(rs)
                    rg.append(rd[i])

                for ij in strings:
                    print(ij)
                for ij in rg:
                    print(ij)
                avg={}
                for r in r_positions.items():
                    avg1=sum(r[1])/len(r[1])
                    avg[r[0]]=avg1
                sorted_footballers_by_goals = sorted(avg.items(), key=lambda x: x[1], reverse=True)
                print(sorted_footballers_by_goals)

                print(f'Processed {line_count} lines.')

def freq___():
    files = os.listdir('D:\Projects\Msc_Research\Protein_Folding\protein_metaheuristics_code')
    m = 0
    files = ['T1033_total.csv']
    for i in files:
        print(i)
        if 'csv' in i:
            print(i)
            with open(i) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                mm = 0
                dict = {}
                atom = []
                rd = []
                r_positions={}
                for row in csv_reader:
                    print(len(row))
                    mm = 0
                    m = 0

                    if line_count == 0:
                        line_count += 1
                        rd = row
                        for ijkp in rd:
                            r_positions[ijkp]=[]
                        print(r_positions)
                    elif line_count == 1:
                        line_count += 1
                        atom = row
                    elif line_count == 2:
                        line_count += 1
                    else:
                        serial = -1

                        best = 1
                        i = 0

                        for ij in row:

                            serial = serial + 1
                            if serial not in dict:
                                dict[serial] = 0
                            if i - 2 > -1:
                                a = row[i - 2]
                            else:
                                a = 0

                            if i - 1 > -1:
                                b = row[i - 1]
                            else:
                                b = 0

                            if i + 1 < len(row):
                                c = row[i + 1]
                            else:
                                c = 0

                            if i + 2 < len(row):
                                d = row[i + 2]
                            else:
                                d = 0

                            ij = (float(a) + float(b) + float(ij) + float(c) + float(d)) / 5
                            if float(ij) > mm:
                                mm = float(ij)
                                best = serial
                            r_positions[rd[serial-1]].append(ij)

                            i = i + 1

                        dict[best] = dict[best] + 1

                        line_count += 1
                sorted_footballers_by_goals = sorted(dict.items(), key=lambda x: x[1], reverse=True)
                print(sorted_footballers_by_goals)
                print(len(sorted_footballers_by_goals))
                top_10 = sorted_footballers_by_goals
                strings = []
                rg = []
                r_pos = {}

                for i55 in top_10:
                    i = i55[0]
                    ul = 0
                    tl = len(rd)
                    if i - 5 > 0:
                        ul = i - 5
                    if i + 5 < len(rd):
                        tl = i + 5

                    rds = ''
                    rs = ''
                    for ijk in range(ul, tl):
                        rs = rs + atom[ijk]

                    strings.append(rs)
                    rg.append(rd[i])

                for ij in strings:
                    print(ij)
                for ij in rg:
                    print(ij)
                avg={}
                for r in r_positions.items():
                    avg1=sum(r[1])/len(r[1])
                    avg[r[0]]=avg1
                sorted_footballers_by_goals = sorted(avg.items(), key=lambda x: x[1], reverse=True)
                print(sorted_footballers_by_goals)

                print(f'Processed {line_count} lines.')
def freq__():
    files=os.listdir('D:\Projects\Msc_Research\Protein_Folding\protein_metaheuristics_code')
    m=0
    files=['T1038_total.csv']
    for i in files :
        print(i)
        if 'csv' in i:
            print(i)
            with open(i) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                mm=0
                dict={}
                atom=[]
                rd=[]
                for row in csv_reader:
                    print(len(row))
                    mm=0
                    m=0

                    if line_count == 0:
                        line_count += 1
                        rd=row
                    elif line_count==1:
                        line_count += 1
                        atom=row
                    elif line_count==2:
                        line_count += 1
                    else:
                        serial=-1

                        best=1
                        i=0

                        for ij in row:


                            serial=serial+1
                            if serial not in dict:
                                dict[serial]=0
                            if i-2>-1:
                                a=row[i-2]
                            else: a=0

                            if i-1>-1:
                                b=row[i-1]
                            else: b=0

                            if i+1< len(row):
                                c=row[i+1]
                            else: c=0

                            if i+2< len(row):
                                d=row[i+2]
                            else: d=0

                            ij=(float(a)+float(b)+float(ij)+float(c)+float(d))/5
                            if float(ij)>mm :

                                mm=float(ij)
                                best=serial

                            i=i+1


                        dict[best]=dict[best]+1






                        line_count += 1
                sorted_footballers_by_goals = sorted(dict.items(), key=lambda x:x[1],reverse=True)
                print(sorted_footballers_by_goals)
                print(len(sorted_footballers_by_goals))
                top_10=sorted_footballers_by_goals
                strings=[]
                rg=[]
                r_pos={}

                for i55 in top_10:
                    i=i55[0]
                    ul=0
                    tl=len(rd)
                    if i-5>0:
                        ul=i-5
                    if i+5<len(rd):
                        tl=i+5


                    rds=''
                    rs=''
                    for ijk in range(ul,tl):
                        rs=rs+atom[ijk]

                    strings.append(rs)
                    rg.append(rd[i])

                for ij in strings:
                    print(ij)
                for ij in rg:
                    print(ij)
                print(f'Processed {line_count} lines.')

#freq_____()

def freq_():
    files=os.listdir('D:\Projects\Msc_Research\Protein_Folding\protein_metaheuristics_code')
    m=0
    files=['T1038.csv']
    for i in files :
        print(i)
        if 'csv' in i:
            print(i)
            with open(i) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                mm=0
                dict={}
                for row in csv_reader:
                    mm=0
                    m=0
                    if line_count == 0:
                        line_count += 1
                    elif line_count==1:
                        line_count += 1
                    elif line_count==2:
                        line_count += 1
                    else:
                        serial=0
                        best=1
                        i=0
                        for ij in row:
                            serial=serial+1
                            if i-2>-1:
                                a=row[i-2]
                            else: a=0

                            if i-1>-1:
                                b=row[i-1]
                            else: b=0

                            if i+1< len(row):
                                c=row[i+1]
                            else: c=0

                            if i+2< len(row):
                                d=row[i+2]
                            else: d=0

                            print(a)
                            print(c)
                            ij=(float(a)+float(b)+float(ij)+float(c)+float(d))/5
                            if float(ij)>mm:
                                mm=float(ij)
                                best=serial
                            i=i+1


                        if best in dict.keys():
                            dict[best]=dict[best]+1

                        else:

                            dict[best]=1
                            dict[best]=dict[best]+1



                        line_count += 1
                sorted_footballers_by_goals = sorted(dict.items(), key=lambda x:x[1],reverse=True)
                print(sorted_footballers_by_goals)

                print(f'Processed {line_count} lines.')



def freq(filename):
    #files=os.listdir('D:\Projects\Msc_Research\Protein_Folding\protein_metaheuristics_code')
    m=0
    files=[]
    files.append(filename)
    for i in files :
        print(i)
        if 'csv' in i:
            print(i)
            with open(i) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                mm=0
                dict={}
                for row in csv_reader:
                    mm=0
                    m=0
                    if line_count == 0:
                        line_count += 1
                    elif line_count==1:
                        line_count += 1
                    elif line_count==2:
                        line_count += 1
                    else:
                        serial=0
                        best=1
                        for ij in row:
                            serial=serial+1
                            if float(ij)>mm:
                                mm=float(ij)
                                best=serial


                        if best in dict.keys():
                            dict[best]=dict[best]+1

                        else:

                            dict[best]=1
                            dict[best]=dict[best]+1



                        line_count += 1
                sorted_footballers_by_goals = sorted(dict.items(), key=lambda x:x[1],reverse=True)
                print(sorted_footballers_by_goals)

                print(f'Processed {line_count} lines.')
                positions = sorted_footballers_by_goals[:40]
                return positions


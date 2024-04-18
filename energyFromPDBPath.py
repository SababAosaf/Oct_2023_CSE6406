import os
import shutil
def energyList(pdbFilePath):


    enegry_calculator_directory='energy_calculation\\'
    for i in os.listdir(enegry_calculator_directory):
        os.remove(enegry_calculator_directory+i)


    if not os.path.exists(enegry_calculator_directory+'foldx.exe'):
        shutil.copy('energy_tools\\foldx.exe',enegry_calculator_directory+'foldx.exe')
        shutil.copy('energy_tools\\rotabase.txt',enegry_calculator_directory+'rotabase.txt')



    shutil.copyfile(pdbFilePath,enegry_calculator_directory+'\\'+os.path.basename(pdbFilePath))
    os.chdir(enegry_calculator_directory)
    command="foldx.exe  --command=Stability --pdb="+os.path.basename(pdbFilePath)
    print(command)
    energy=os.popen(command).read()


    ij= energy.index('Total          =') + len('Total          =')
    lines=energy.split('\n')
    energies=[]
    for j in lines:
        if '=' in j:

            j=j.split('=')
            j[0]=j[0].strip()
            j[1]=j[1].strip()
            energies.append((j[0],j[1]))


    ik=energy.index('\n',ij)
    energy=energy[ij:ik]

    os.chdir('..')
    return energies

def energyFromPDBPath(pdbFilePath):


    enegry_calculator_directory='energy_calculation\\'
    for i in os.listdir(enegry_calculator_directory):
        os.remove(enegry_calculator_directory+i)


    if not os.path.exists(enegry_calculator_directory+'foldx.exe'):
        shutil.copy('energy_tools\\foldx.exe',enegry_calculator_directory+'foldx.exe')
        shutil.copy('energy_tools\\rotabase.txt',enegry_calculator_directory+'rotabase.txt')



    shutil.copyfile(pdbFilePath,enegry_calculator_directory+'\\'+os.path.basename(pdbFilePath))
    os.chdir(enegry_calculator_directory)

    command="foldx.exe  --command=Stability --pdb="+os.path.basename(pdbFilePath)

    energy=os.popen(command).read()



    ij= energy.index('Total          =') + len('Total          =')
    ik=energy.index('\n',ij)
    energy=energy[ij:ik]



    os.chdir('..')
    return float(energy.strip())


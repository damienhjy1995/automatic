import os
import subprocess as sub
import re

curdir=os.getcwd()
curdir=curdir.strip('automatic')
newdir=curdir+'inputdata'
os.chdir(newdir)#enter data directory
with open('input.txt','r') as f:
    count=len(f.readlines())
    f.seek(0)
    for i in range(1,count+1):
        line=f.readline()
        find_1=bool(re.match('[\s]*casetype',line))
        find_2=bool(re.match('[\s]*num_p_pre',line))
        find_3=bool(re.match('[\s]*num_p_solve',line))
        find_4=bool(re.match('[\s]*inputpath',line))
        find_5=bool(re.match('[\s]*meshtype',line))
        find_6=bool(re.match('[\s]*internalfield',line))
        find_7=bool(re.match('[\s]*mediumtype',line))
        find_8=bool(re.match('[\s]*quadtype',line))
        find_9=bool(re.match('[\s]*spacescheme',line))
        find_10=bool(re.match('[\s]*wall_temperature',line))
        find_11=bool(re.match('[\s]*wall_emissivity',line))
        find_12=bool(re.match('[\s]*num_p_dir',line))
        find_13=bool(re.match('[\s]*n_axis',line))
        if find_1 == True:
            casetype=line.lstrip()
            casetype=casetype.replace('casetype = ','')
            casetype=casetype.rstrip()
        if find_2 == True:
            num_pre=line.lstrip()
            num_pre=num_pre.replace('num_p_pre = ','')
            num_pre=num_pre.rstrip()
        if find_3 == True:
            num_solve=line.lstrip()
            num_solve=num_solve.replace('num_p_solve = ','')
            num_solve=num_solve.rstrip()
        if find_4 == True:
            inputpath=line.lstrip()
            inputpath=inputpath.replace('inputpath = ','')
            inputpath=inputpath.rstrip()
        if find_5 == True:
            meshtype=line.lstrip()
            meshtype=meshtype.replace('meshtype = ','')
            meshtype=meshtype.rstrip()
        if find_6 == True:
            internalfield=line.lstrip()
            internalfield=internalfield.replace('internalfield = ','')
            internalfield=internalfield.rstrip()
        if find_7 == True:
            mediumtype=line.lstrip()
            mediumtype=mediumtype.replace('mediumtype = ','')
            mediumtype=mediumtype.rstrip()
        if find_8 == True:
            quadtype=line.lstrip()
            quadtype=quadtype.replace('quadtype = ','')
            quadtype=quadtype.rstrip()
        if find_9 == True:
            spacescheme=line.lstrip()
            spacescheme=spacescheme.replace('spacescheme = ','')
            spacescheme=spacescheme.rstrip()
        if find_10 == True:
            wall_temperature=line.lstrip()
            wall_temperature=wall_temperature.replace('wall_temperature = ','')
            wall_temperature=wall_temperature.rstrip()
        if find_11 == True:
            wall_emissivity=line.lstrip()
            wall_emissivity=wall_emissivity.replace('wall_emissivity = ','')
            wall_emissivity=wall_emissivity.rstrip()
        if find_12 == True:
            num_p_dir=line.lstrip()
            num_p_dir=num_p_dir.replace('num_p_dir = ','')
            num_p_dir=num_p_dir.rstrip()
        if find_13 == True:
            n_axis=line.lstrip()
            n_axis=n_axis.replace('n_axis = ','')
            n_axis=n_axis.rstrip()

with open('input_2.txt','w') as c:
    print('#inputpath',file=c)
    print(inputpath,file=c)
    print('#meshtype',file=c)
    print(meshtype,file=c)
    print('#casetype',file=c)
    print(casetype,file=c)
    print('#internalfield',file=c)
    print(internalfield,file=c)
    print('#mediumtype',file=c)
    print(mediumtype,file=c)
    print('#quadtype',file=c)
    print(quadtype,file=c)
    print('#spacescheme',file=c)
    print(spacescheme,file=c)
    print('#wall_temperature',file=c)
    print(wall_temperature,file=c)
    print('#wall_emissivity',file=c)
    print(wall_emissivity,file=c)
    print('#num_p_dir',file=c)
    print(num_p_dir,file=c)
    print('#n_axis',file=c)
    print(n_axis,file=c)

if casetype == 'benchmark':#if the case is a benchmark,just trim the primitive .msh file
    newdir=curdir+'convert_msh'
    os.chdir(newdir)#change directory to convert_msh
    job=sub.call('./launch',shell=True)
elif casetype == 'real':#if the case is a real case with .dat file, convert it to the modified .msh file
    newdir=curdir+'dat_2_msh'
    os.chdir(newdir)#change directory to new_pre
    job=sub.call('./launch',shell=True)

newdir=curdir+'preprocessing'
os.chdir(newdir)#enter preprocessing directory
job=sub.call('./launch',shell=True)
job=sub.call('./pre',shell=True)
newdir=curdir+'solver'
os.chdir(newdir)#enter solver directory
job=sub.call('./launch',shell=True)
job=sub.call('mpirun -np '+num_solve+ ' ./solve',shell=True)
newdir=curdir+'postprocessing'#enter postprocessing directory
os.chdir(newdir)
job=sub.call('./launch',shell=True)
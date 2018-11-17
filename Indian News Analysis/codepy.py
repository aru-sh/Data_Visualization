import os
os.chdir('c:\\Users\Arush\Desktop')
import pandas as pd
df=pd.read_csv('dvproject.csv',sep=',',header=None, low_memory=False, encoding = 'ISO-8859-1')
aar=df.values

mon=[];
tue=[];
wed=[];
thu=[];
fri=[];
sat=[];
sun=[];

pmon=0
ptue=0
pwed=0
pthu=0
pfri=0
psat=0
psun=0

nmon=0
ntue=0
nwed=0
nthu=0
nfri=0
nsat=0
nsun=0

nemon=0
netue=0
newed=0
nethu=0
nefri=0
nesat=0
nesun=0


for i in range(1,683838):
    day=aar[i][4]
    sent=aar[i][6]
    
    if(day=='Mon'):
        if(sent=='pos'):
            pmon+=1
        elif(sent=='neg'):
            nmon+=1
        elif(sent=='neu'):
            nemon+=1

    elif(day=='Tue'):
        if(sent=='pos'):
            ptue+=1
        elif(sent=='neg'):
            ntue+=1
        elif(sent=='neu'):
            netue+=1
            
    elif(day=='Wed'):
        if(sent=='pos'):
            pwed+=1
        elif(sent=='neg'):
            nwed+=1
        elif(sent=='neu'):
            newed+=1

    elif(day=='Thu'):
        if(sent=='pos'):
            pthu+=1
        elif(sent=='neg'):
            nthu+=1
        elif(sent=='neu'):
            nethu+=1

    elif(day=='Fri'):
        if(sent=='pos'):
            pfri+=1
        elif(sent=='neg'):
            nfri+=1
        elif(sent=='neu'):
            nefri+=1

    elif(day=='Sat'):
        if(sent=='pos'):
            psat+=1
        elif(sent=='neg'):
            nsat+=1
        elif(sent=='neu'):
            nesat+=1

    elif(day=='Sun'):
        if(sent=='pos'):
            psun+=1
        elif(sent=='neg'):
            nsun+=1
        elif(sent=='neu'):
            nesun+=1


mon.append(pmon)
mon.append(nmon)
mon.append(nemon)

tue.append(ptue)
tue.append(ntue)
tue.append(netue)

wed.append(pwed)
wed.append(nwed)
wed.append(newed)

thu.append(pthu)
thu.append(nthu)
thu.append(nethu)

fri.append(pfri)
fri.append(nfri)
fri.append(nefri)

sat.append(psat)
sat.append(nsat)
sat.append(nesat)

sun.append(psun)
sun.append(nsun)
sun.append(nesun)
	

import os
os.chdir('c:\\Users\Arush\Desktop')
import pandas as pd
df=pd.read_csv('dvproject.csv',sep=',',header=None, low_memory=False, encoding = 'ISO-8859-1')
aar=df.values

jan=[]
feb=[]
mar=[]
apr=[]
may=[]
jun=[]
jul=[]
aug=[]
sep=[]
octu=[]
nov=[]
dec=[]


pjan=0
pfeb=0
pmar=0
papr=0
pmay=0
pjun=0
pjul=0
paug=0
psep=0
poctu=0
pnov=0
pdec=0

njan=0
nfeb=0
nmar=0
napr=0
nmay=0
njun=0
njul=0
naug=0
nsep=0
noctu=0
nnov=0
ndec=0

nejan=0
nefeb=0
nemar=0
neapr=0
nemay=0
nejun=0
nejul=0
neaug=0
nesep=0
neoctu=0
nenov=0
nedec=0




for i in range(1,683838):
    mon=aar[i][1]
    sent=aar[i][6]
    
    if(mon=="1"):
        if(sent=='pos'):
            pjan+=1
        elif(sent=='neg'):
            njan+=1
        elif(sent=='neu'):
            nejan+=1

    elif(mon=="2"):
        if(sent=='pos'):
            pfeb+=1
        elif(sent=='neg'):
            nfeb+=1
        elif(sent=='neu'):
            nefeb+=1
            
    elif(mon=="3"):
        if(sent=='pos'):
            pmar+=1
        elif(sent=='neg'):
            nmar+=1
        elif(sent=='neu'):
            nemar+=1

    elif(mon=="4"):
        if(sent=='pos'):
            papr+=1
        elif(sent=='neg'):
            napr+=1
        elif(sent=='neu'):
            neapr+=1

    elif(mon=="5"):
        if(sent=='pos'):
            pmay+=1
        elif(sent=='neg'):
            nmay+=1
        elif(sent=='neu'):
            nemay+=1

    elif(mon=="6"):
        if(sent=='pos'):
            pjun+=1
        elif(sent=='neg'):
            njun+=1
        elif(sent=='neu'):
            nejun+=1

    elif(mon=="7"):
        if(sent=='pos'):
            pjul+=1
        elif(sent=='neg'):
            njul+=1
        elif(sent=='neu'):
            nejul+=1

    elif(mon=="8"):
        if(sent=='pos'):
            paug+=1
        elif(sent=='neg'):
            naug+=1
        elif(sent=='neu'):
            neaug+=1

    elif(mon=="9"):
        if(sent=='pos'):
            psep+=1
        elif(sent=='neg'):
            nsep+=1
        elif(sent=='neu'):
            nesep+=1

    elif(mon=="10"):
        if(sent=='pos'):
            poctu+=1
        elif(sent=='neg'):
            noctu+=1
        elif(sent=='neu'):
            neoctu+=1

    if(mon=="11"):
        if(sent=='pos'):
            pnov+=1
        elif(sent=='neg'):
            nnov+=1
        elif(sent=='neu'):
            nenov+=1

    elif(mon=="12"):
        if(sent=='pos'):
            pdec+=1
        elif(sent=='neg'):
            ndec+=1
        elif(sent=='neu'):
            nedec+=1



jan.append(pjan)
jan.append(njan)
jan.append(nejan)

feb.append(pfeb)
feb.append(nfeb)
feb.append(nefeb)

mar.append(pmar)
mar.append(nmar)
mar.append(nemar)

apr.append(papr)
apr.append(napr)
apr.append(neapr)

may.append(pmay)
may.append(nmay)
may.append(nemay)

jun.append(pjun)
jun.append(njun)
jun.append(nejun)

jul.append(pjul)
jul.append(njul)
jul.append(nejul)

aug.append(paug)
aug.append(naug)
aug.append(neaug)

sep.append(psep)
sep.append(nsep)
sep.append(nesep)


octu.append(poctu)
octu.append(noctu)
octu.append(neoctu)

nov.append(pnov)
nov.append(nnov)
nov.append(nenov)

dec.append(pdec)
dec.append(ndec)
dec.append(nedec)

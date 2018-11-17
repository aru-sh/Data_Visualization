import os
import pandas as pd
os.chdir('c:\\Users\Arush\Desktop')
df=pd.read_csv('dvproject.csv',sep=',',header=None, low_memory=False, encoding = 'ISO-8859-1')
aar=df.values
words={"kohli":0}


for i in range(1,683835):
    head=aar[i][5]
    for w in head.split():
        if w in words:
            aar[i][8]=1

for i in range(1,683835):
    if(aar[i][8]==1):
        aar[i][8]=1
    else:
        aar[i][8]=0

#for i in range(1,683835):
for i in range(1,683835):
    senti=aar[i][6]
    
    if(aar[i][8]==1):
        if(senti=="pos"):
            aar[i][9]=1
            aar[i][10]=0
            aar[i][11]=0
        elif(senti=="neg"):
            aar[i][9]=0
            aar[i][10]=1
            aar[i][11]=0
        elif(senti=="neu"):
            aar[i][9]=0
            aar[i][10]=0
            aar[i][11]=1
            
    elif(aar[i][8]==0):
        aar[i][9]=0
        aar[i][10]=0
        aar[i][11]=0


df=pd.DataFrame(aar)

df.to_csv("kohli.csv",sep=',')

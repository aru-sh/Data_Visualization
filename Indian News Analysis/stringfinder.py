import os
import pandas as pd
os.chdir('c:\\Users\Arush\Desktop')
df=pd.read_csv('dvproject.csv',sep=',',header=None, low_memory=False, encoding = 'ISO-8859-1')
aar=df.values
words={"modi":0}


for i in range(1,683835):
    head=aar[i][5]
    for w in head.split():
        if w in words:
            aar[i][8]=1

df=pd.DataFrame(aar)

df.to_csv("modi.csv",sep=',')

import os
import pandas as pd
os.chdir('c:\\Users\Arush\Desktop')
df=pd.read_csv('modi.csv',sep=',',header=None, low_memory=False, encoding = 'ISO-8859-1')
aar=df.values
words={"modi":0}


for i in range(1,683835):
    senti=aar[i][7]
    
    if(aar[i][9]=="1"):
        if(senti=="pos"):
            aar[i][10]=1
            aar[i][11]=0
            aar[i][12]=0
        elif(senti=="neg"):
            aar[i][10]=0
            aar[i][11]=1
            aar[i][12]=0
        elif(senti=="neu"):
            aar[i][10]=0
            aar[i][11]=0
            aar[i][12]=1
            
    elif(aar[i][9]=="0"):
        aar[i][10]=0
        aar[i][11]=0
        aar[i][12]=0
        
df=pd.DataFrame(aar)

df.to_csv("modi2.csv",sep=',')

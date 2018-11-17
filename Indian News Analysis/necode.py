import os
import pandas as pd
os.chdir('c:\\Users\Arush\Desktop')
from nltk.tokenize import RegexpTokenizer

df=pd.read_csv('dvproject.csv',sep=',',header=None, low_memory=False, encoding = 'ISO-8859-1')
tokenizer = RegexpTokenizer(r'\w+')
#s="yr main's m!!??,, ffasdf,, .. aahaha AAAA !!?";
#s=s.lower()
#out=tokenizer.tokenize(s)

aar=df.values

headlinenew=[]

for i  in range(1,683838):
    headline=(aar[i][5]).lower()
    out=tokenizer.tokenize(headline)
    headlinenew.append(" ".join(str(x) for x in out))


df=pd.DataFrame(headlinenew)
df.to_csv("newnew1.csv",sep=',')

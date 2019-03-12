'''
this is application-specific, do not execute it anymore
'''

import pandas as pd
import numpy as np

df = pd.read_excel("data/gre3000.xlsx")
print(df.dtypes)

listNow=-1
unitNow=-1

for index,row in df.iterrows():
    '''
    if not pd.isnull(df.loc[index,"List"]):
        listNow=df.loc[index,"List"]
    df.loc[index, "list"]=listNow
    if not pd.isnull(df.loc[index,"Unit"]):
        unitNow=df.loc[index,"Unit"]
    df.loc[index, "unit"]=unitNow
    '''

    df.loc[index,"英文单词"]=df.loc[index,"英文单词"].strip()
    df.loc[index, "correct"]=0
    df.loc[index, "notSure"]=0
    df.loc[index, "wrong"]=0
    df.loc[index, "history"]=""
    df.loc[index, "发音文件"] = "notExist"
    df.loc[index, "音标"] = "notExist"
    df.loc[index,"comment"]=""


with pd.ExcelWriter('data/gre3000.xlsx') as writer:
    df.to_excel(writer)

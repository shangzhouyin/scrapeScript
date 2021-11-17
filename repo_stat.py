import os 
import pandas as pd 
import csv
import numpy as np
from pandas.core.reshape.merge import merge

path = "/Users/yinshangzhou/desktop/script/test2"
path2 = "/Users/yinshangzhou/desktop/script/test2/grpc-master.csv"
file_extension = ".csv"
new_file = "data.csv"
os.chdir(path)
f = pd.read_csv(path2)
f.set_index("Language")
file_name = []
for filename in os.listdir(path):
    if filename == "grpc-master.csv":
        continue
    elif(os.path.splitext(filename)[1] == file_extension and filename!= new_file):
        t = os.path.splitext(filename)[0]
        file_name.append(t + file_extension)
for fi in file_name:
    df1 = pd.read_csv(fi)
    f = f.merge(df1, how='left', on='Language').fillna(0)
    #df2 = df2.merge(df1,how = 'right', on = 'Language')
f.set_index('Language')
# for col in  f.columns[1:]:
#     f[col] = pd.to_numeric(f[col], errors='coerce')
m = f.loc[:,['code1','code2','code3','code4','code5','code6','code7','code8','code9','code10','code11']]
m['median'] = m.median(axis = 1)
f = f.merge(m, how='right', on='code1')
print(f)

f.to_csv(r'/Users/yinshangzhou/desktop/script/test2/data.csv', index = False)
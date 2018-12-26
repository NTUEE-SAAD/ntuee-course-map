import numpy as np
import pandas as pd

data = pd.read_csv("../dat/compulsory.csv",sep=',', header=None) #專題

data.sort_values(1)
data = data.fillna(0)

prof = data.get(0)
domain = data.get(1)
content1 = data.get(2)

f = open('../result/compulsory.md', 'w')

for i in range(len(data)):
    f.write("> " + str(prof[i]) + "\n\n")
    f.write("* 相關領域：" + str(domain[i]) + "\n")
    f.write("* 專題小卦：\n")
    if content1[i] != 0:
        tmp = content1[i].replace('\n', '')
        f.write("  1. " + tmp + "\n")
    f.write("\n")


# In[ ]:




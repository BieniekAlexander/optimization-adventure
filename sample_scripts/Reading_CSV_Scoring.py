#!/usr/bin/env python
# coding: utf-8

# In[110]:


import pandas as pd
from sklearn.metrics import mean_squared_error
from math import sqrt

IIHS = pd.read_csv (r'/Users/dominic/Dropbox (EEC)/PC Transfer/Dominic/optimization-adventure/IIHS_lac.csv', skiprows=4, na_values = None, encoding = "UTF-8")
IIHS = IIHS.rename(columns= {' /2/1006 ( /Scaled_Hybrid_III_50th/HeadCG_acc ) CFC1000 - Res. acceleration (m/s**2)': 'HRes',
                       ' /2/1006 ( /Scaled_Hybrid_III_50th/HeadCG_acc ) CFC1000 - X-comp. acceleration (m/s**2)': 'HX',
                       ' /2/1006 ( /Scaled_Hybrid_III_50th/HeadCG_acc ) CFC1000 - Y-comp. acceleration (m/s**2)': 'HY',
                       ' /2/1006 ( /Scaled_Hybrid_III_50th/HeadCG_acc ) CFC1000 - Z-comp. acceleration (m/s**2)': 'HZ',
                       ' /2/6004 ( /Scaled_Hybrid_III_50th/Pelvis_acc ) CFC1000 - Res. acceleration (m/s**2)': 'PRes',
                       ' /2/6004 ( /Scaled_Hybrid_III_50th/Pelvis_acc ) CFC1000 - X-comp. acceleration (m/s**2)': 'PX',
                       ' /2/6004 ( /Scaled_Hybrid_III_50th/Pelvis_acc ) CFC1000 - Y-comp. acceleration (m/s**2)': 'PY',
                       ' /2/6004 ( /Scaled_Hybrid_III_50th/Pelvis_acc ) CFC1000 - Z-comp. acceleration (m/s**2)': 'PZ'})
IIHS = IIHS.dropna()
MadOut = pd.read_csv (r'/Users/dominic/Dropbox (EEC)/PC Transfer/Dominic/optimization-adventure/Madymo_lac.csv', skiprows=4, na_values = None, encoding = "UTF-8")
MadOut = MadOut.rename(columns= {' /2/1006 ( /Scaled_Hybrid_III_50th/HeadCG_acc ) CFC1000 - Res. acceleration (m/s**2)': 'HRes',
                       ' /2/1006 ( /Scaled_Hybrid_III_50th/HeadCG_acc ) CFC1000 - X-comp. acceleration (m/s**2)': 'HX',
                       ' /2/1006 ( /Scaled_Hybrid_III_50th/HeadCG_acc ) CFC1000 - Y-comp. acceleration (m/s**2)': 'HY',
                       ' /2/1006 ( /Scaled_Hybrid_III_50th/HeadCG_acc ) CFC1000 - Z-comp. acceleration (m/s**2)': 'HZ',
                       ' /2/6004 ( /Scaled_Hybrid_III_50th/Pelvis_acc ) CFC1000 - Res. acceleration (m/s**2)': 'PRes',
                       ' /2/6004 ( /Scaled_Hybrid_III_50th/Pelvis_acc ) CFC1000 - X-comp. acceleration (m/s**2)': 'PX',
                       ' /2/6004 ( /Scaled_Hybrid_III_50th/Pelvis_acc ) CFC1000 - Y-comp. acceleration (m/s**2)': 'PY',
                       ' /2/6004 ( /Scaled_Hybrid_III_50th/Pelvis_acc ) CFC1000 - Z-comp. acceleration (m/s**2)': 'PZ'})

MadOut = MadOut.dropna()
IIHS_list = list(IIHS.columns)
Mad_list = list(MadOut.columns)
Score = 0.0

for i in range(1,len(IIHS_list)):
    I_HRes = IIHS[IIHS_list[i]]
    M_HRes = MadOut[Mad_list[i]]
    rms = sqrt(mean_squared_error(I_HRes, M_HRes))
    Score = Score + rms

print (Score)


# 

# In[ ]:





# In[ ]:





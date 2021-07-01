# %%
# imports
import pandas as pd
from sklearn.metrics import mean_squared_error
from math import sqrt
import numpy as np
import sys
import os


# %%
def get_madymo_summary(path_to_csv):
    """
    Retrieve the results of a Madymo experiment, from a CSV, and put them into a dataframe

    TODO this implementation probably makes a ton of assumptions about the contents of the experiment result CSV,
    maybe revisit this implementation to generalize it more?
    """
    df = pd.read_csv(path_to_csv, skiprows=4, na_values = None, encoding = "UTF-8")
    df = df.rename(columns= {' /2/1006 ( /Scaled_Hybrid_III_50th/HeadCG_acc ) CFC1000 - Res. acceleration (m/s**2)': 'HRes',
                       ' /2/1006 ( /Scaled_Hybrid_III_50th/HeadCG_acc ) CFC1000 - X-comp. acceleration (m/s**2)': 'HX',
                       ' /2/1006 ( /Scaled_Hybrid_III_50th/HeadCG_acc ) CFC1000 - Y-comp. acceleration (m/s**2)': 'HY',
                       ' /2/1006 ( /Scaled_Hybrid_III_50th/HeadCG_acc ) CFC1000 - Z-comp. acceleration (m/s**2)': 'HZ',
                       ' /2/6004 ( /Scaled_Hybrid_III_50th/Pelvis_acc ) CFC1000 - Res. acceleration (m/s**2)': 'PRes',
                       ' /2/6004 ( /Scaled_Hybrid_III_50th/Pelvis_acc ) CFC1000 - X-comp. acceleration (m/s**2)': 'PX',
                       ' /2/6004 ( /Scaled_Hybrid_III_50th/Pelvis_acc ) CFC1000 - Y-comp. acceleration (m/s**2)': 'PY',
                       ' /2/6004 ( /Scaled_Hybrid_III_50th/Pelvis_acc ) CFC1000 - Z-comp. acceleration (m/s**2)': 'PZ'})

    df = df.dropna()
    return df


# %%
def get_dfs_rmse(df1, df2):
    """
    Get the RMSE of two pandas dataframes

    https://statweb.stanford.edu/~susan/courses/s60/split/node60.html
    """
    # asssert that the arrays have the same contents
    assert(list(df1.columns)==list(df2.columns))
    assert(df1.shape == df2.shape)
    # TODO maybe add more assertions - how do we know that we can actually compute RMSE of these two dataframes?

    a = df1.values ; b = df2.values
    return np.sqrt(np.mean((a-b)**2))


# %%
# simple, convenient tests, if this is the sccript being invoked
if __name__ == "__main__":
    # verifying RMSE calculation
    # for x0, x1, RMSE = 36.90323 -> https://www.statology.org/rmse-calculator/
    x0 = [1,5,100,23.3,44,50.4]
    x1 = [2,3,10.3,21.3,40,60.4]

    rmse = get_dfs_rmse(pd.DataFrame(x0), pd.DataFrame(x1))
    print(rmse)

import os
import glob
import functools
import pandas as pd


DATA_DIR = 'data'


def read_as_dataframe():
    """
    Read all files into one single dataframe.
    PS: this should work, unfortunately, my computer is slow to load all into one. 
    I didn't try this code, but if this works, you only need to loop for the rows.
    """
    par_func = functools.partial(pd.read_csv, compression='bz2', encoding='ISO-8859-1', memory_map=True)
    file_list = glob.glob(os.path.join(DATA_DIR, '*.csv.bz2'))
    df = pd.concat(map(par_func, file_list))

    return df
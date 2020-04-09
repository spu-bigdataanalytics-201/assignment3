import os
import glob
import functools
import pandas as pd


def read_as_dataframe(num_of_files=5):
    """
    Read all files into one single dataframe.
    
    Notes:
    This function will work only if you have a large amount of RAM
    on your computer. For example, anything above 30 GB should work.

    If you have less RAM, you can limit the number of files to load
    with this function with the parameter.

    For more information on this issue, check out the stackoverflow
    answer: https://datascience.stackexchange.com/a/27794/61094.

    Parameters:
    num_of_files - How many files from the data folder you want to
                   load to.
    """
    # partial function
    par_func = functools.partial(
        pd.read_csv, 
        compression='bz2', 
        engine='c', 
        low_memory=True
    )

    # file path list
    file_list = list(glob.glob('data/*.csv.bz2'))

    # run partial function for all file paths and concat the dataframe
    df = pd.concat(map(par_func, file_list[:num_of_files]))

    return df

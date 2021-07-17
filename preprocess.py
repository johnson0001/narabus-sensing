import os
import glob
import numpy as np
import pandas as pd

# separate stamp data and adrs data from original data 
def separate_stamp(filepath):
    global stamp_data, adrs
    try:
        csv = pd.read_csv(filepath)
    except:
        print("No data in {}".format(os.path.split(filepath)[1]))
    else:
        stamp_data = csv.columns.values
        adrs = np.delete(csv.values, 0, 0)
        adrs = pd.DataFrame(adrs, columns=['address', 'rssi', 'uuid'])

    return stamp_data, adrs

# extract files of specific id
def file_extraction(dir_name, id):
    file_list = sorted(os.listdir(dir_name))
    file_list = [file for file in file_list if file.split('_')[0] == str(id)]
    if not file_list:
        return print("No correct file of ID:{}".format(id))
    else:
        return file_list
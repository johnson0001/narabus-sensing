import os
import re
import glob
import numpy as np
import pandas as pd

# separate stamp data and address data from original data 
def separateStampAndAdrs(filePath):
    global stamp, adrs
    try:
        csv = pd.read_csv(filePath)
    except:
        print("No data in {}".format(os.path.split(filePath)[1]))
    else:
        stamp = csv.columns.values
        adrs = np.delete(csv.values, 0, 0)
        adrs = pd.DataFrame(adrs, columns=['address', 'rssi', 'uuid'])

    return stamp, adrs

# extract files of correct data of specific id
def fromCorrectFolder(correctFolderPath, raspID):
    filesAll = sorted(os.listdir(correctFolderPath))
    files = [file for file in filesAll if file.split('_')[0] == str(raspID)]
    if not files:
        return print("No correct file of ID:{}".format(raspID))
    else:
        return files

# extract files of experiment time
def duringEx(allFiles, startExTime, finishExTime=None):
    firstIdx = next(idx for idx, filePath in enumerate(allFiles) if re.search(startExTime, filePath))
    if finishExTime == None:
        return allFiles[int(firstIdx):]
    else:
        lastIdx = next((idx for idx, filePath in enumerate(allFiles) if re.search(finishExTime, filePath)), -1)
        if lastIdx == -1:
            return allFiles[int(firstIdx):]
        else:
            return allFiles[int(firstIdx):int(lastIdx)]


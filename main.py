import os
import re
import glob
import pandas as pd
import preprocess

# Experiment Date
exDate = 20210704

# Start and Finish Time of Experiment
startExTime = str(exDate) + "09"
finishExTime = str(exDate) + "16"

# Raspberry Pi ID
raspID = 2000

# Data Directry
rawDir = "./rawdata_" + str(exDate) + "/"
correctDir = "./correct_record/"

# Output Directry
stampDfDir = "./data_" + str(exDate) + "/"
adrsDfDir = stampDfDir + str(raspID) + "/"

def main():
    stampList = []
    adrsList = []
    files = glob.glob(rawDir + str(raspID) + "/*.csv")
    files = sorted(files)
    ### extract files of experiment time ###
    # files = preprocess.duringEx(files, startExTime)
    for filePath in files:
        stamp, adrs = preprocess.separateStampAndAdrs(filePath)
        stampList.append(stamp)
        adrsList.append(adrs)
        ### create csv of adrs ###
        fileName = os.path.basename(filePath)
        adrs.to_csv(adrsDfDir + fileName)
    
    ### create csv of stamp list ###
    stampDF = pd.DataFrame(
        stampList,
        columns=['time', 'latitude', 'longitude'])
    stampDF.to_csv(stampDfDir + str(raspID) + "_scan_list.csv")
    
    # print(stampList[0])
    # print(adrsList[0])
        
    # correctFiles = preprocess.fromCorrectFolder(correctDir, raspID)
    
if __name__ == '__main__':
    main()
    # preprocess.file_extraction(correct_dir, rasp_id)
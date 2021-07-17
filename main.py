import glob
import preprocess

# Raspberry Pi ID
rasp_id = 2000

# Data Directry
data_dir = "./raspi_origin/"
correct_dir = "./correct_record/"

def main():
    stamp_list = []
    adrs_list = []
    files = glob.glob(data_dir + str(rasp_id) + "/*.csv")
    for filepath in files:
        stamp_data, adrs = preprocess.separate_stamp(filepath)
        stamp_list.append(stamp_data)
        adrs_list.append(adrs)
    # print(stamp_list[0])
    # print(adrs_list[0])
        
    correct_files = preprocess.file_extraction(correct_dir, rasp_id)
    

if __name__ == '__main__':
    # main()
    # preprocess.file_extraction(correct_dir, rasp_id)
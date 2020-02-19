import csv
import os
from pathlib import Path
from csv import DictWriter

keywords = ["temp_sector", "company_name", "ml", "machine", "learning", "data", "science", "big", "analysis", "analytics",
"artificial", "intelligent", "face", "recognition", "video", "computer", "vision", "optical", "biometric", "biometrics", 
"iot", "blockchain", "warehouse", "cloud", "hosting", "security", "attendance", "cctv", "ip", "camera", "retail",
"chat", "rmg", "fmcg", "commerce", "e-commerce", "storage", "vat", "isp", "training","networking", "infrastructure",
"bank", "erp", "pos", "startups", "ekyc", "government", "govt"]


path = '/home/nilim/Documents/SoftExpo2020Text'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))

for path in files:
    # print(path)
    split_value = path.split('/')
    sector = split_value[5]
    company_name = split_value[6]
    file_name = split_value[7].split('.')
    file_raw_name = file_name[0]

    print(file_raw_name)

    # user_search_value = "learning"
    word_count_obj = {}
    word_count_obj['temp_sector'] = sector
    word_count_obj['company_name'] = company_name

    print(word_count_obj)
    for value in keywords[2:]:
        # print('value', value)
        #read file
        filename = path
        f = open(filename, "r")
        lines = f.readlines()
        f.close()
        #looking for patterns
        count = 0
        for line in lines:
            line = line.strip().lower().split()
            # print(line)
            for words in line:
                if words.find(value.lower()) != -1:
                    count += 1
        word_count_obj[value] = count
        # print("\nYour search value of '%s' appears %s times in this file" % (value, count))

    # print('asd', word_count_obj)
    # f = open('csv_store/names.csv', 'a')


    with open('csv_store/names.csv', 'a', newline='') as f:
    # with open('csv_store/names.csv', 'a+', newline='') as write_obj:
        # keywords.insert(0, "company_name")
        # keywords.insert(0, "temp_sector")
        # fnames = ['first_name', 'last_name']

        writer = csv.DictWriter(f, fieldnames=keywords)

        f.seek(0, 2)

        if f.tell() == 0:
            writer.writeheader()



        print('word_count_obj', word_count_obj)
        writer.writerow(word_count_obj)

        # word_count_obj = {}
        # dict_writer = DictWriter(write_obj, fieldnames=keywords)
        # dict_writer.writerow(word_count_obj)

        f.close()



# keywords = {"temp_sector": 'sum', "company_name": 'sum', "ml": 'sum', "machine": 'sum', "learning": 'sum', "data": 'sum', "science": 'sum', "big": 'sum', "analysis": 'sum', "analytics": 'sum',
# "artificial": 'sum', "intelligent": 'sum', "face": 'sum', "recognition": 'sum', "video": 'sum', "computer": 'sum', "vision": 'sum', "optical": 'sum', "biometric": 'sum', 
# "iot": 'sum', "blockchain": 'sum', "warehouse": 'sum', "cloud": 'sum', "hosting": 'sum', "security": 'sum', "attendance": 'sum', "cctv": 'sum', "ip": 'sum', "camera": 'sum', "retail": 'sum',
# "rmg": 'sum', "fmcg": 'sum', "commerce": 'sum', "e-commerce": 'sum', "storage": 'sum', "vat": 'sum', "isp": 'sum', "training": 'sum',"networking": 'sum', "infrastructure": 'sum',
# "bank": 'sum', "erp": 'sum', "pos": 'sum', "startups": 'sum', "ekyc": 'sum', "government": 'sum', "govt": 'sum'}
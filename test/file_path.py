import os
from pathlib import Path

path = '/home/nilim/Documents/SoftExpo2020'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.pdf' in file:
            files.append(os.path.join(r, file))

for path in files:
    print(path)
    base_path = '/home/nilim/Documents/'
    text_path = 'SoftExpo2020Text'
    img_path = 'SoftExpo2020Img'

    split_value = path.split('/')
    sector = split_value[5]
    company_name = split_value[6]
    file_name = split_value[7].split('.')
    file_raw_name = file_name[0]

    print(file_raw_name)

    create_dir_img = f"{base_path}/{img_path}/{sector}/{company_name}"
    Path(create_dir_img).mkdir(parents=True, exist_ok=True)

    create_dir_txt = f"{base_path}/{text_path}/{sector}/{company_name}"
    Path(create_dir_img).mkdir(parents=True, exist_ok=True)

    

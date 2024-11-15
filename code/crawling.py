import os
import pandas as pd

folder_path = 'D:/Personal/Desktop/electricitymaps/config/zones'

data = []

for filename in os.listdir(folder_path):
    if filename.startswith('US'):  # "US"
        file_path = os.path.join(folder_path, filename)
        
        with open(file_path, 'r') as file:
            lines = file.readlines()

            if len(lines) >= 5:  
                row = [filename]
                for i in range(1, 5):  
                    line = lines[i].strip()
                    number = ''.join(filter(lambda x: x.isdigit() or x == '.', line))
                    row.append(number)
                data.append(row)

df = pd.DataFrame(data, columns=['File Name', 'Line 2', 'Line 3', 'Line 4', 'Line 5'])

df.to_excel('output.xlsx', index=False)

print('成功')

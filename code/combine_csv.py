import os
import pandas as pd

def merge_csv_files_in_folder(folder_path, output_file):
    # 获取文件夹中所有的csv文件
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    
    # 创建一个空的DataFrame用于存放合并后的数据
    combined_csv = pd.DataFrame()
    
    # 遍历每一个csv文件并将其数据追加到combined_csv
    for file in csv_files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        combined_csv = pd.concat([combined_csv, df], ignore_index=True)
    
    # 将合并后的数据写入一个新的csv文件
    combined_csv.to_csv(output_file, index=False)
    print(f"All files have been merged into {output_file}")

# 示例用法
folder_path = 'D:/Personal/Desktop/Elec_document/Address_DC(BA)'  # 替换为你的文件夹路径
output_file = 'Address_DC(BA).csv'    # 替换为你想要保存的合并后的文件名
merge_csv_files_in_folder(folder_path, output_file)

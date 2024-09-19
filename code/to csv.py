import os
import pandas as pd

def convert_xlsx_to_csv(directory):
    # 检查指定路径是否存在
    if not os.path.exists(directory):
        print(f"路径 '{directory}' 不存在")
        return

    # 获取指定路径下的所有文件
    files = os.listdir(directory)

    # 遍历所有文件
    for file in files:
        # 检查文件是否为.xlsx文件
        if file.endswith('.xlsx'):
            # 生成完整的文件路径
            file_path = os.path.join(directory, file)
            
            # 读取.xlsx文件
            try:
                df = pd.read_excel(file_path)
            except Exception as e:
                print(f"读取文件 '{file}' 失败: {e}")
                continue
            
            # 生成.csv文件的文件名
            csv_file = file.replace('.xlsx', '.csv')
            csv_path = os.path.join(directory, csv_file)
            
            # 保存为.csv文件
            try:
                df.to_csv(csv_path, index=False)
                print(f"成功转换: {file} -> {csv_file}")
            except Exception as e:
                print(f"保存文件 '{csv_file}' 失败: {e}")

if __name__ == "__main__":
    # 指定文件夹路径
    folder_path = "E:/pythonTest/result"
    convert_xlsx_to_csv(folder_path)

import pandas as pd

def remove_characters_in_column(file_path, sheet_name, column_name, characters_to_remove, output_file):
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # 删除指定列中的字符
    df[column_name] = df[column_name].str.replace(f"[{characters_to_remove}]", "", regex=True)

    df.to_excel(output_file, index=False)

file_path = 'BA_Address.xlsx'
sheet_name = 'Sheet1'
column_name = 'File Name'
characters_to_remove = ".yaml"
output_file = 'output.xlsx'

remove_characters_in_column(file_path, sheet_name, column_name, characters_to_remove, output_file)

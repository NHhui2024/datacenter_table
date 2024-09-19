import pandas as pd
import os

first_excel_path = 'DC_Address.xlsx'
second_excel_path = 'BA_Address.xlsx'
no_match_excel = "defult.xlsx"
output_folder = 'E:/pythonTest/result'

first_df = pd.read_excel(first_excel_path)

second_df = pd.read_excel(second_excel_path)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for index, row in first_df.iterrows():
    first_col_value_1 = row[0]
    first_col_value_2 = row[1]
    first_col_value_3 = row[2]

    matched = False

    for index, row in second_df.iterrows():
        second_col_value_2 = row[1]
        second_col_value_3 = row[2]
        second_col_value_4 = row[3]
        second_col_value_5 = row[4]

        if first_col_value_2 >= second_col_value_2 and first_col_value_2 <= second_col_value_4 and first_col_value_3 >= second_col_value_3 and first_col_value_3 <= second_col_value_5:
            output_filename = f"{row[0]}.xlsx"
            output_filepath = os.path.join(output_folder, output_filename)
        
            if os.path.exists(output_filepath):
                output_df = pd.read_excel(output_filepath)
                output_df = output_df._append({'Data': first_col_value_1}, ignore_index=True)
            else:
                output_df = pd.DataFrame({'Data': [first_col_value_1]})
            
            output_df.to_excel(output_filepath, index=False)
            #print(f'完成{first_col_value_1}')
            matched = True
            break

    if not matched:
        """
        if not os.path.exists(no_match_filepath):
            no_match_df = pd.DataFrame(columns=['Unmatched'])
            no_match_df.to_excel(no_match_excel_path, index=False)
        """
        no_match_filepath = os.path.join(output_folder, no_match_excel)
        no_match_df = pd.read_excel(no_match_filepath)
        no_match_df = no_match_df._append({'Unmatched': first_col_value_1}, ignore_index=True)
        no_match_df.to_excel(no_match_filepath, index=False)
        print(f'完成{first_col_value_1}')

print('完成')



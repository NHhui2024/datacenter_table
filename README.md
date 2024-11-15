
Document list
1.Introduction
  This project collected the data of electricity demand, carbon emission and new energy ratio of Balance Authority(BA) in the United States, classified the data centers according to the regions of BA, and calculated its electricity consumption and carbon emissions.
Firstly, BA's hourly Electricity consumption data(Data_elec_BA) is downloaded from eia's official website and BA's hourly carbon emission data(Data_carbon_BA) is downloaded from Electricity map website, and then according to BA's name and UTC time, the ‘Demand’ column in the electricity consumption data table is merged with the carbon emission data into the required data(Combine_elec_carbon).
Then, Information about the Data Center is available on the data center map website, include name, number, and state of the data centers(Data_DC). The address of the data centers are obtained through Google Maps and converted to latitude and longitude(Address_DC). Total electricity consumption of data centers in each state can be found in reference ‘Powering Intelligence Analyzing Artificial Intelligence and Data Center Energy Consumption’ on page 28-29. For the missing data in the literature, regression models can be used to make predictions(Data_elec_DC). Then take the average as electricity consumption of each data center. For carbon emissions of data centers, it can be calculated by multiplying the electricity consumption of a data center with the carbon intensity of the BA to which the data center belongs.
For the determination of BA region, the source code of electricity map was downloaded from GitHub, the bonding box of BA(Address_BA) was extracted by python script and compared with the longitude and dimension of data centers(Address_DC) to obtain the table of data center division by BA region(Address_DC(BA)).
Finally, organize the name, location, power consumption, carbon emissions, and BA of the data center into the file ‘merge.csv’.
Details of the documents can be found below.
2.Initial documentation description
1)Data_elec_BA: Balance Authority(BA) electricity consumption data
Time: 2015-2023 hourly
Available content: BA,UTC time,Demand
Data Source: https://www.eia.gov/electricity/gridmonitor/dashboard/electric_overview/US48/US48
2)Data_carbon_BA: BA's carbon emissions data
Time: 2021-2023 hourly
Available content: Zone ID, UTC time, Carbon Intensity, Low Carbon Percentage, Renewable Percentage
Data Source: https://www.electricitymaps.com/data-portal/united-states-of-america
3)Data_DC: DC's name, number, state
Data Source: https://www.datacentermap.com/datacenters/
method to obtain: 
Xpath code:
//*[@id="__next"]/div/div/div[2]/main/div/div[2]/div[3]/div/a[/]/div/div[2]
4)Data_elec_DC: The electricity consumption of data centers
Data Source: Powering Intelligence Analyzing Artificial Intelligence and Data Center Energy Consumption
Regression model code:
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data provided by the user
data_new = np.array([
    99280, 77200.83951, 33566.97482, 27448, 4380,
    11252.68293, 73516.55952, 1095, 29784, 49338.91391,
    5071.578947, 206444, 625.7142857, 81030, 6570,
    5256, 3568.888889, 20830.76471, 10305.88235, 18318.13333,
    24309, 192720, 232912.9412, 85417.675, 1946.666667,
    60274.02985, 44773.33333, 31776.44531, 43814.36066, 559388.5714,
    15153.11538, 51100, 58840.94495, 65574.85714, 2920,
    134904, 17520, 28850.86957, 78464.60072, 94890.25926,
    71566.85412, 58108, 3918.947368, 185712
])
n_states_new = 44
X_new = np.arange(n_states_new).reshape(-1, 1)
model_new = LinearRegression()
model_new.fit(X_new, data_new)
X_pred_new = np.arange(n_states_new, n_states_new + 7).reshape(-1, 1)
y_pred_new = model_new.predict(X_pred_new)
X_full = np.arange(n_states_new + 7)
data_full = np.concatenate([data_new, y_pred_new])
plt.figure(figsize=(10, 6))
plt.plot(X_new, data_new, 'bo', label='Existing Data')
plt.plot(X_pred_new, y_pred_new, 'ro', label='Predicted Data')
plt.plot(X_full, data_full, 'g-', label='Regression Line')
plt.xlabel('Index')
plt.ylabel('Data Value')
plt.title('Linear Regression Model: Existing and Predicted Data')
plt.legend()
plt.grid(True)
plt.show()
5)Address_BA: BA's bounding-box
Data Source: https://github.com/electricitymaps/electricitymaps-contrib/tree/master/config/zones
method to obtain: 
for filename in os.listdir(folder_path):
    if filename.startswith('US'):  # "US"
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
Code function: Extract the numbers and '. 'in lines 2-5 of the corresponding file.
6)Address_DC: DC's latitude and longitude
Data Source: https://www.datacentermap.com/datacenters/ and https://maplocation.sjfkai.com
method to obtain:
The address of Data Centers are obtained through Xpath in https://www.datacentermap.com/datacenters/. Xpath code is as follows.
//*[@id="__next"]/div/div/div[2]/main/div/div[2]/div[3]/div/a[/]/div/div[3]/text()[2]
Then through https://maplocation.sjfkai.com batch convert Data Centers' location to latitude and longitude. Notice: The website has a limited number of enquiries per day.

For the few that cannot be converted directly, you can mark them on Google Maps and obtain latitude and longitude.
3.Merge document descriptions
1)Combine_elec_carbon: 2023 BA's electricity consumption and carbon emission related data
method to obtain: 
Merge BA, UTC time, and Demand in Data_elec_BA with Carbon Intensity, Low Carbon Percentage, and Renewable Percentage in Data_carbon_BA.
2)Address_DC(BA):Data centers in each BA
method to obtain: 
for index, row in first_df.iterrows():
    first_col_value_1 = row[0]
    first_col_value_2 = row[1]
    first_col_value_3 = row[2]

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
            print(f'完成{first_col_value_1}')
            break
Code function:
Take columns B and C of DC_Address and columns B,D,C,E of BA_Address. If the data in column B of DC_Address is between the data in columns B and D of BA_Address, and the data in column C of DC_Address is between the data in columns C and E of BA_Address, Put the name of the data center into an excel file named BA, or create one if there is no such file.


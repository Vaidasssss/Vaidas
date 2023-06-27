# ##### LENTELIŲ KŪRIMAS IR JŲ ĮVAIRIŲ FORMŲ PERTEIKIMAS
#
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
#
# # # #### vienmate  duomenu struktura kuri saugo eilutes duomenis su indeksais
# # data = pd.Series([10, 20 , 30, 40, 50])
# # print(data)
# #
# #
# # # ####Dvimate duomenu struktura kuri saugo duomenis lenteles pavidalu su stulpeliu ir eiluciu indeksais
# # data = {'Name' : ['Mantas', 'Deividas', 'Migle', 'Ausrine'],
# #         'Age' : [29, 26, 27, 56],
# #         'City' : ['Marijampole', 'Vilnius', 'Kaunas', 'Vilnius']
# #         }
# #
# # df = pd.DataFrame(data)
# # ####Atvaizduoja visa lentele
# # print(df)
# #
# #
# # ####Atvaizduojame pirmas 4 eilutes DataFrame
# # print(df.head(4))
# #
# #
# # ####Atvaizduoja stulpelius
# # select_columns = df[['Name', 'Age']]
# # print(select_columns)
# #
# # ####Prideti nauja stulpeli
# # df['Salary'] = [1600, 1400, 1300, 1200]
# #
# #
# # print(df)
# #
# # ####grupuokime duomenis pagal miesta ir gaukite vidutini atlyginima
# # average_salary_by_city = df.groupby('City')['Salary'].mean()
# # print(average_salary_by_city)
# #
# # ####skaiciuosja amziaus vidurki
# # average_age = df['Age'].mean()
# # print(f"Vidutinis amzius {average_age}")
# #
# # #### filtruoja amzius aks daugiau nei 30 metu
# # filtered_data = df[df['Age'] > 30][['Name', 'Age']]
# # print(filtered_data)
# #
# # #### filtruoja amziu ir rodo du tik stulpelius
# # filtered_data = df[df['Age'] > 30][['Name', 'Age']]
# # print(filtered_data)
#

file_path= Path('employees.csv')
df = pd.read_csv(file_path)
print(df.head(5))
#
# # ### grupuoti pagal 'first_name' stulepeli ir suskaičiuoti jo dydį
# # group_sizes = df.groupby('FIRST_NAME').size()
# #
group_average = df.groupby('FIRST_NAME')['SALARY']. mean()

group_stats = df.groupby('FIRST_NAME')['SALARY'].describe()

group_max = df.groupby('FIRST_NAME')['SALARY'].max()

group_agg = df.groupby('FIRST_NAME').agg({'SALARY': ['sum', 'mean', 'max']})


#### atvaizduojama linijinė diagrama
group_agg.plot(kind='bar')
#### pridedamos diagramos antrastės
plt.title('Suveskite statistika pagal jų vardus ir atlyginimus')
plt.xlabel('Vardas')
plt.ylabel('Atlyginimas')

###atvazduoja diagrama
plt.show()
#
#

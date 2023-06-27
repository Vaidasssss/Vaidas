import pandas as pd
from pathlib import Path
file_path= Path('employees1.csv')
df = pd.read_csv(file_path)
import matplotlib.pyplot as plt
# # print(df)

## Atlyginimų statistika pagal JOB_ID. Grupuoja ir apskaičiuoja atlyginimų vidurikį, aukščiausią atlyginimą
## bei mažiausią atlyginimą

# vidurkis = df.groupby('JOB_ID')['SALARY'].mean()
# minimusmas = df.groupby('JOB_ID')['SALARY'].min()
# maximumas = df.groupby('JOB_ID')['SALARY'].max()
# bendras = df.groupby('JOB_ID').agg({'SALARY':['mean', 'max', 'min']})
#
# bendras.plot(kind='bar')
# plt.title('Atlyginimų statistika pagal JOB_ID')
# plt.xlabel('JOB_ID')
# plt.ylabel('Atlyginimas')
# plt.show()

##Panaikina DEPARTMENT_ID dublikatus ir grąžina tris stulpelius
# dublikatai = df.drop_duplicates('DEPARTMENT_ID')[['FIRST_NAME', 'LAST_NAME', 'JOB_ID']]
# print(dublikatai)


## Sukuriami stulpeliai, jais manipuliuojama ir atvaizduojama diagramoje
# df['PILNASVARDAS'] = df['FIRST_NAME']+ ' ' +df['LAST_NAME']
# df['PAKELTAS_ATLYGINIMAS'] = df['SALARY'] * 1.15
# nadojami=['PILNASVARDAS','PAKELTAS_ATLYGINIMAS','SALARY' ]
#
# df[nadojami].plot(kind='bar')
# plt.title('ATLYGINIMŲ KITIMAS')
# plt.xlabel('DARBUOTOJAS')
# plt.ylabel('Atlyginimas')
# plt.show()


# # pagal kiekvineo JOB ID parodo maximalu alyginima
# maxjob = df.groupby('JOB_ID')['SALARY'].max()
#
# # pasalina JOB ID dublikatus
# dublikatai = df.drop_duplicates('JOB_ID')
#
# # atlyginimo pakelimas naujame stulpelyje
# df['PAKELTAS_ATLYGINIMAS'] = df.SALARY * 1.15
#
#
# print(df)


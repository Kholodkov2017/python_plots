import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.axis as ax

# подключение кб бд
conn = pyodbc.connect('Driver={SQL Server};'
                    'Server=DESKTOP-656KKVV\SQLEXPRESS01;'
                    'Database=zdb;'
                    'Trusted_Connection=yes;')


sql = 'Select Data.year as Год, SUM(Data.pk) as ОбщаяЧисленностьСтудентов from Data group by Data.year ORDER BY Data.Year'
plt.figure(1)
# fig, axs = plt.subplots(nrows= 3 , ncols= 1 )
data = pd.read_sql(sql,conn)
plt.plot(data['Год'], data['ОбщаяЧисленностьСтудентов'], color='red', marker="o")
# plt.ticklabel_format(style='scientific', axis='y', useOffset=False)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.title('График динамики численности студентов')
plt.ylabel('Динамика численности')
plt.xlabel('Год')


plt.figure(2)
sql2 = 'Select Data.federal_district_short as [Федеральный округ], SUM(Data.total_income) as Доход from Data where year = 2016 group by Data.federal_district_short order by Доход'
data2 = pd.read_sql(sql2,conn)
plt.bar(data2['Федеральный округ'], data2['Доход'])
# plt.ticklabel_format(style='scientific', axis='y', useOffset=False)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.title('Гистограмма общих доходов по федеральным округами за 2016 год')
plt.ylabel('Доход')
plt.xlabel('Федеральный округ')

plt.figure(3)
sql3 = "select Data.region_name [Регион],  sum(Data.rnd) [Объем НИОКР] from Data where Data.federal_district_short = 'ПФО' and year = 2016 group by Data.region_name"
data3 =  pd.read_sql(sql3,conn)
plt.pie(data3['Объем НИОКР'], labels=data3['Регион'], autopct='%1.1f%%')
plt.title('Объем НИОКР по субъектам в Приволжском ФО за 2016 год')
plt.show()


import pyodbc # библиотека для работы с бд
import pandas as pd # библиотека для обработки и анализа структурированных данных
import matplotlib.pyplot as plt # модуль для создания графики

# подключение кб бд
conn = pyodbc.connect('Driver={SQL Server};'
                    'Server=DESKTOP-656KKVV\SQLEXPRESS01;'
                    'Database=zdb;'
                    'Trusted_Connection=yes;')


#запрос данных к бд
sql = 'Select Data.year as Год, SUM(Data.pk) as ОбщаяЧисленностьСтудентов from Data group by Data.year ORDER BY Data.Year'

# создаем отдельный график
plt.figure(1)

# выбираем данные по запросу
data = pd.read_sql(sql,conn)

# строим график по полученным данным
plt.plot(data['Год'], data['ОбщаяЧисленностьСтудентов'], color='red', marker="o")

# рисуем сетку графика
plt.grid(color = 'green', linestyle = '--', linewidth = 1)

# Добавляем легенду к графикам
plt.title('График динамики численности студентов')
plt.ylabel('Динамика численности')
plt.xlabel('Год')

# создаем отдельный график
plt.figure(2)

#строка запроса данных к бд
sql2 = 'Select Data.federal_district_short as [Федеральный округ], SUM(Data.total_income) as Доход from Data where year = 2016 group by Data.federal_district_short order by Доход'

# выбираем данные по запросу
data2 = pd.read_sql(sql2,conn)

# рисуем график
plt.bar(data2['Федеральный округ'], data2['Доход'])

# рисуем сетку графика
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

# Добавляем легенду к графикам
plt.title('Гистограмма общих доходов по федеральным округами за 2016 год')
plt.ylabel('Доход')
plt.xlabel('Федеральный округ')

# создаем отдельный график
plt.figure(3)

#строка запроса данных к бд
sql3 = "select Data.region_name [Регион],  sum(Data.rnd) [Объем НИОКР] from Data where Data.federal_district_short = 'ПФО' and year = 2016 group by Data.region_name"

# выбираем данные по запросу
data3 =  pd.read_sql(sql3,conn)

# рисуем график
plt.pie(data3['Объем НИОКР'], labels=data3['Регион'], autopct='%1.1f%%')

# Добавляем легенду к графикамф
plt.title('Объем НИОКР по субъектам в Приволжском ФО за 2016 год')

# отображаем графики
plt.show()


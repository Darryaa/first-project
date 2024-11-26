#!/usr/bin/env python
# coding: utf-8

# <div class="alert alert-success">
# <font size="5", color = "seagreen"><b>✔️ Комментарий ревьюера в4</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Привет, Дарья :)
#     
# Спасибо за работу на проекте, за все исправления и комментарии
#          
#         
# Подведем итоги, мы научились и повторили на проекте каким образом:
# 
# + читать тех. задание проекта
# + исследовать неочищенные данные
# + выдвигать гипотезы о пропусках данных и заполнять их значениями
# + принимать решения об удалении некачественных данных
# + находить аномалии в данных и отделять редкие значения
# + соглашаться с наличием пропусков в данных и не забывать об их наличии при фильтрации
# + строить информативные визуализации
# + делить одну выборку на две части
# + находить зависимости и распределения в данных 
# + формировать выводы
#         
# Навыки отработаны, проект принят 
# 
# <b>Поздравляю с успешно сданным третьим проектом на факультете дата-аналитики Я.Практикум</b>
# 
# <div class="alert alert-success">
#     <font size="5", color = "seagreen"><b>Успехов в дальнейшей учебе 🤝</b></font><br />
#     
# добавил бонус и новые подсказки с пометкой в4

# <div class="alert alert-success">
# <font size="5", color= "seagreen"><b>✔️ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Привет, Дарья :)
#         
# Критические ❌ комментарии
# 
#          
# + сменить тип данных
# + добавить гистограммы в п.4.1         
# + настроить фильтрацию редких значений 
# + добавить вывод в раздел о скорости продаж         
# + добавить вывод в п. 4.3
# + исследовать аномалию в п.4.5
# + поправить итоговый вывод
#            
# добавил новых подсказок        
#       

# <div class="alert alert-success">
# <font size="4"><b>Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
#     Привет, Дарья :) Спасибо за доработки 🤝  Добавил новых подсказок на второй версии проверки

# <div class="alert alert-success">
# <font size="4"><b>Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
#     Привет, Дарья :) Спасибо, что прислала задание 🤝 Меня зовут Ринат Хисамов и я буду проверять твой проект. Предлагаю обращаться друг к другу на ты. Так нам будет гораздо проще и удобней общаться
# 
# Мои комментарии обозначены пометкой <b>Комментарий ревьюера</b>. Далее в файле сможешь найти их в похожих ячейках (если фон комментария зелёный — всё сделано правильно (✔️), рекомендации таким же цветом. Отдельным цветом — блок ссылок (примеры ниже, 🍕). Оранжевым или светло желтым рекомендации, которые, хоть и не обязательны, но точно сделают ревью лучше. (⚠️); <u> красный комментарий</u>: код, график или вывод стоит переделать (❌)). 
# 
# Не удаляй все эти комментарии и постарайся учесть их в ходе выполнения данного проекта. 
# Будет замечательно, если добавишь свои комментарии и пояснения✍
#         
# Поехали 🚀
#     <br />
#     </font>
# 
# </div>

# <div style="border:solid steelblue 1px; padding: 20px">
#     
# <font size="4"><p style="text-align:center"><b>Примеры комментариев </b></p></font>
#     
# <div style="border:solid steelblue 3px; padding: 20px">
# <font size="4"><b>🍕 Пример комментария - совета, здесь м.б. просто ссылка</b></font>
#     <br /> 
#         <font size="3", color = "black">
# <br />
#     Тут всего такого разного и вкусного :), есть способы прокачать проект визуализациями (ценит большинство "боссов")  <br /><br />
#         <a href="https://devpractice.ru/matplotlib-book/">“Библиотека Matplotlib” доступна для скачивания БЕСПЛАТНО!</a>
#         На сайте много полезных материалов, мне самому очень помогло в свое время, до сих пор подсматриваю :)
# 
# 
# </div>
#     
# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
#     <font size="3"><b>⚠️ Пример оформления некритичного комментария</b>
#     <br /> 
#     <font size="2", color = "black">
# <br />
#     Рекомендации, которые, хоть и не обязательны, но точно сделают ревью лучше
#     <br />
#     </font>
# 
# </div>
#     
# <div class="alert alert-danger">
# <font size="3"><b>❌ Пример оформления комментария к блоку(строке) программного кода (или выводу), который стоит переделать</b></font>
#     <br /> 
#     <font size="2", color = "black">
# <br />
#     Отправлен не тот проект, напиши в своих комментариях, что случилось? жду — <b>это пример</b>
#     <br />
#     </font>
# 
# </div>
#     
# <div class="alert alert-success">
# <font size="4"><b>✔️ Пример оформления комментария, который нравится большинству студентов</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
#     Круто, молодец, отлично, логично, или — 👌, 👍, или — выводы отвечают на все вопросы к данным и проекту
#     <br />
#     </font>
# 
# </div>

# # Для твоих вопросов или комментариев оставлю такую ячейку, чтобы было удобнее взаимодействовать на проекте

# <div class="alert alert-info">
# <font size="4", color = "black"><b>✍ Комментарий студента</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Привет! Огромное спасибо за подробный разбор, было наглядно и полезно! Отправляю очередную версию: здесь я сознательно поправила только код и воздержалась от каких-либо выводов, поскольку не уверена в технической стороне, на основе которой их хорошо было бы делать:) Понимаю, что все это чревато последствиями и доработоками, но хотела сначала убедиться, что технически все сделано относительно корректно. 
#         

# <div style>
# <font size="4"><b></b></font>
# <font size="5", color = "black">
# 🤝

# # Исследование объявлений о продаже квартир
# 
# В вашем распоряжении данные сервиса Яндекс Недвижимость — архив объявлений о продаже квартир в Санкт-Петербурге и соседних населённых пунктах за несколько лет. Вам нужно научиться определять рыночную стоимость объектов недвижимости. Для этого проведите исследовательский анализ данных и установите параметры, влияющие на цену объектов. Это позволит построить автоматизированную систему: она отследит аномалии и мошенническую деятельность.
# 
# По каждой квартире на продажу доступны два вида данных. Первые вписаны пользователем, вторые — получены автоматически на основе картографических данных. Например, расстояние до центра, аэропорта и других объектов — эти данные автоматически получены из геосервисов. Количество парков и водоёмов также заполняется без участия пользователя.

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
# Название, краткое вступление в работу и главная задача зафиксированы. 
#        
#         
# Четкий план работ и перечень основных задач позволит коллегам быстрее вникнуть в суть проекта, + будет легче  идти к главной цели проекта

# ## Шаг 1. Откройте файл с данными и изучите общую информацию

# In[1]:


import pandas as pd
import datetime 
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
import warnings
import plotly.express as px 
warnings.simplefilter(action='ignore', category=FutureWarning)


# In[2]:


df = pd.read_csv("/datasets/real_estate_data.csv",delimiter="\t")
df.head()


# In[3]:


df.hist(figsize=(15, 20));


# ## Шаг 2. Выполните предобработку данных

# In[4]:


df.isna().sum()


# ### check

# In[5]:


# check
df.info()


# <div class="alert alert-dan ger">
# <font size="4"><b>❌ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />                  
# Слишком жесткое условие для фильтрации выборки ⬆⬆⬆
#         
# __Если при одной фильтрации, на этом проекте, теряем больше одного процента данных от изначального объема, стоит еще раз пересмотреть условия фильтрации__
#         
# 

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />  
#         
#         
#         df.drop_duplicates(subset=['last_price', 'total_area',"floors_total"],keep='first', inplace=True, ignore_index=False)
#         
# На этом проекте мы лишь учимся исследовать подобные записи, вполне возможно, что публиковали объявления о продаже одинаковых квартир из соседних подъездов, стоит смотреть на сами записи перед удалением
#         
#         чтобы посмотреть на все записи (оригинал + дубликат) используем параметр 
#         
#         keep=False
#         
#         можно добавить к сумме колонок — дату публикации объявления

# In[6]:


#заполняем медианным значением пропуски в airports_nearest
air_table = df.pivot_table(index="locality_name",values="airports_nearest",aggfunc="median")
for a in air_table.index:
    df.loc[(df['locality_name'] == a) & (df['airports_nearest'].isna()), 'airports_nearest'] =     df.loc[(df['locality_name'] == a),'airports_nearest'].median()
df[df["airports_nearest"].isna()]    


# In[7]:


#заполняем медианным значением пропуски в cityCenters_nearest 
center_table = df.pivot_table(index="locality_name",values="cityCenters_nearest",aggfunc="median")
for a in center_table.index:
    df.loc[(df['locality_name'] == a) & (df['cityCenters_nearest'].isna()), 'cityCenters_nearest'] =     df.loc[(df['locality_name'] == a),'cityCenters_nearest'].median()
df[df["cityCenters_nearest"].isna()]


# In[8]:


#заполняем медианным значением пропуски в parks_around3000
a = df.pivot_table(index="locality_name",values="parks_around3000",aggfunc="mean")
a = a.query("parks_around3000 == 0")
for a in a.index:
    df.loc[(df['locality_name'] == a) & (df['parks_around3000'].isna()), 'parks_around3000'] =     df.loc[(df['locality_name'] == a),"parks_around3000"].mean()
df[df["parks_around3000"].isna()]


# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />         
# Стоит доработать
#         
#         'посёлок городского типа мга',
#         'городской посёлок мга'
#         
# Можно отметить в отчете — стоит ли объединять нас. пункты
#         
#         'деревня Кудрово' 
#         'Кудрово'

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Стоит исследовать выборку
#        
#         
# + __на простое дублирование записей__
#  + __особенно это станет важным, когда мы перейдем к более сложным задачам на втором модуле курса__
#         
# <br />  
#         
# + дополнительно — на рабочих проектах стоит искать дубликаты по сумме ключевых параметров (подмножеству), для примера: 
# 
#  + общ. площадь квартиры,
#  + этаж, 
#  + общая этажность дома, 
#  + расстояние до центра
#  + название населенного пункта
#  + кол-во комнат
#     
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html?highlight=duplicat#pandas.DataFrame.duplicated
#         
# https://www.codecamp.ru/blog/pandas-find-duplicates/        

# In[9]:


#заполняем пропущенные значения в balcony
df["balcony"] = df["balcony"].fillna(0)


# In[10]:


df.dropna(subset=["locality_name"],inplace=True)
df
#locality_name важная для исследования информация,поэтому удаляем строки с пропусками в этом столбце


# ### 2.2

# In[11]:


#меняем тип данных
df["first_day_exposition"] = pd.to_datetime(df["first_day_exposition"], errors='coerce')
df["kitchen_area"] = np.floor(pd.to_numeric(df["kitchen_area"], errors='coerce')).astype('Int64')
df["days_exposition"] = np.floor(pd.to_numeric(df["days_exposition"], errors='coerce')).astype('Int64')
df["floors_total"] = np.floor(pd.to_numeric(df["floors_total"], errors='coerce')).astype('Int64')
df["balcony"] = np.floor(pd.to_numeric(df["balcony"], errors='coerce')).astype('Int64')


# ### 2.3

# In[12]:


#проверяем дубликаты в столбце locality_name
#cоздание список слов, подлежащих удалению в названиях для привидения их к однообразию
remove = ["деревня","посёлок городского типа","поселок городского типа","посёлок при железнодорожной станции","городской поселок","городской посёлок","поселок","посёлок","село","садоводческое некоммерческое товарищество","садовое товарищество","коттеджный","станции"]
for a in remove:
    df["locality_name"] = df["locality_name"].str.replace(a,'') 
df['locality_name'] = df['locality_name'].str.strip()
print("всего уникальных названий:", len(df.sort_values(by="locality_name")["locality_name"].unique()))


# In[13]:


#ищем дубликаты, фильтруем по локации, цене, общей и жилой площади, этажу
df.sort_values(by="last_price")[df.duplicated(subset=["last_price","total_area","locality_name","living_area","floor"],keep=False)]


# In[14]:


#удаляем дубликаты
df.drop_duplicates(subset=["last_price","total_area","locality_name","living_area","floor"],keep='first', inplace=True, ignore_index=False)
df


# <div style="border:solid steelblue 3px; padding: 20px">
# <font size="4">🍕<b> Комментарий ревьюера</b></font>
# <br /> 
# <font size="3", color = "black">
# <br /> Наглядность представления информации одна из важных составляющих работы дата-аналитика или дата-сайентиста
#     
# __мой график оформлен не совсем корректно, сможешь отметить, что стоило бы исправить в графике?__
#   

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера в2</b></font>
#     <br />  
#     <font size="3", color = "black">
# <br /> не помешает добавить вывод после первого знакомства с данными

# In[15]:


df.dropna(subset=["floors_total"],inplace=True)
df.isna().sum()


# В рамках первичной обработки данных было выявлено необнообразие в названиях локации. Были удалены описательные вставки в названиях, такие как поселок, деревня и тд и оставлены исключительно названия. 
# 
# Были также обнаружены дубликаты по нескольким ключевым показателям, которые были удалены. Были удалены пропуски в floors_total
# 
# Данные в first_day_exposition были изменены из типа object в datetime для дальнейшего использования методов для типа datetime, кроме того был изменен тип days_exposition, тк здесь представлены целые числа. Был измнен тип данных в «balcony» и «floors_total», тк здесь представлены целые числа. В других столбцах тип данных не был изменен, тк они будут округляться в дальнейшем анализе.
# 
# В balcony пропуски были заменены на нулевые значения.
# 
# Медианными значениями были дополнены параметры расстояния по парка и аэропорта.

# ##  Шаг 3. Добавьте в таблицу новые столбцы

# #### check

# In[16]:


#проверяем уникальные значения в этажах, чтобы избежать нулевые значения 
print(df["floor"].sort_values().unique())
#проверяем пропуски
print("пропусков:",df["floor"].isna().sum())

#добавляем столбец floor_cat с тремя категориями: первый, последний и другой
first = (df["floor"] == 1)
last = (df["floor"] == df["floors_total"])
df["floor_cat"] = df["floor"]
df.loc[last,"floor_cat"] = "последний"
df.loc[first,"floor_cat"] = "первый"
with warnings.catch_warnings():
    warnings.simplefilter(action='ignore', category=FutureWarning)
    df["floor_cat"][(df["floor_cat"] != "первый") & (df["floor_cat"] != "последний")] = "другой"
   # df["floor_cat"][(df["floor_cat"] != "первый") & (df["floor_cat"] != "последний")] = "другой"


# 

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Функция хорошая, стоит учесть крайние условия: возможные нулевые и отрицательные значения
#         
# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ ответ в2</b></font>
#             <br /> 
#     <font size="3", color = "black">
# <br /> перед применением функции проверила на возможные нулевые и отрицательные значения
#         
#         

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />в следующем месяце мы можем работать с базой недвижимости Москвы или Торонто, в которых могут встретиться полуподвальные или подвальные помещения ... или нам предоставили только часть датасета ...
#         
# универсальная функция ценится тем, что её программируют один раз, а используют множество раз, например для средних этажей добавить такую проверку
#         
#           elif 1 < floor < floors_total:

# 

# In[17]:


#добавляем столбец price, где указана цена за кв.метр 
df["price"] = df["last_price"] / df["total_area"]
df["price"] = df["price"].round(2)
df.head()


# In[18]:


#добавляем столбец to_center, где указано расстояние до центра города в км
df["to_center"] = df["cityCenters_nearest"]/1000
df["to_center"] = df["to_center"].apply(np.floor)
df["to_center"] = df["to_center"].astype("Int64")
df.head()


# <div class="alert alert-dang er">
# <font size="4"><b>❌ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />стоит выполнить пункт проекта
#         
# •	расстояние до центра города в километрах (переведите из м в км и __округлите до целых значений__).
#       

# done 

# In[19]:


#добавляем столбец day, где указан день публикации
week_days = []
for a in df["first_day_exposition"]:
    week_days.append(a.weekday())
df1 = pd.DataFrame(week_days)
df1.columns = ["date"]
df["week_day"] = df1["date"]
df.head()


# In[20]:


#добавляем столбец year, где указан год публикации
df['year'] = pd.DatetimeIndex(df['first_day_exposition']).year
#добавляем столбец month, где указан месяц публикации
df['month'] = pd.DatetimeIndex(df['first_day_exposition']).month
df.head()


# ## Шаг 4. Проведите исследовательский анализ данных:

# In[21]:


#для первичного знакомства с данных вызываем фунцкию описания
#замечаем аномальные минимальные и максимальные значения в
#floor, total_area,ceiling_height,last_price,kitchen_area
df.describe()



# In[22]:


#смотрим на минимальные значения
df["ceiling_height"].hist(bins = 100, figsize = (15,3),range=(1,1.5),grid=True);


# In[23]:


#смотрим на максимальные значения
df["ceiling_height"].hist(bins = 100, figsize = (15,3),range=(10,100),grid=True);


# In[24]:


odd = (df["ceiling_height"] >= 20)
#исправляем подозрительно высокие значения в ceiling_height
df.loc[odd,"ceiling_height"] = df[odd]["ceiling_height"] * 0.1


# In[25]:


df.query("ceiling_height > 4")["ceiling_height"].hist(bins = 10, figsize = (15,3));
df = df.drop(df[df['ceiling_height'] > 4].index)


# In[26]:


df.query("ceiling_height < 2.4")["ceiling_height"].hist(bins = 100, figsize = (15,3));


# In[27]:


df = df.drop(df[df['ceiling_height'] < 2.4].index)


# In[28]:


#cмотрим на количество комнат
df.rooms.hist(bins = 19, figsize = (15,3),range=(0,20));


# <div class="alert alert-danger">
# <font size="4"><b>❌ Комментарий ревьюера в4</b></font>
#     <br />
#     <font size="3", color = "black">
# <br />  Стоит изменить параметры отображения гистограммы (добавить кол-во корзин), сейчас трудно определить типовое кол-во комнат
#         
# ![image.png](attachment:image.png)        

# In[29]:


#заменяем 0-комнатные на 1-комнатные
zero = (df["rooms"] == 0)
df.loc[zero,"rooms"] = 1


# In[30]:


#удаляем квартиры с более чем 5 комнатами,тк их количество незначительно
df = df.drop(df[df["rooms"] > 5].index)


# In[31]:


#строим гистограмму и удаляем нерепрезентативные значения
df["days_exposition"].hist()
df.query("days_exposition > 1100")
df = df.drop(df[df["days_exposition"] > 1100].index)


# In[32]:


#удаляем подозрительно низкие значения
df["days_exposition"].hist(range=(0,20))
df.query("days_exposition < 4")
df = df.drop(df[df["days_exposition"] < 4].index)
df["days_exposition"].hist(range=(0,20));


# In[33]:


#смотрим на подозрительно низкие значения в общей площади, удаляем их
df.living_area.hist(range=(1,14))
df.query("living_area < 11")
df = df.drop(df[df["living_area"] < 11].index)


# In[34]:


#смотрим на подозрительно высокие значения в общей площади, удаляем их

df.living_area.hist(range=(100,410));
df.query("living_area >110")
df = df.drop(df[df["living_area"] > 110].index)


# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера в4</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Хорошие графики, можно увеличить кол-во корзин у  гистограмм и изменить размер у графиков (увеличить ширину)
# 
# Подписи осей на графиках и название добавят ясности и читабельности.
# Это важные элементы любой визуализации. Как добавить подписи и названия, смотри [здесь](https://proproprogs.ru/modules/matplotlib-razmeshchaem-standartnye-tekstovye-elementy-na-grafike?ysclid=l6agtioc6f299002507)
#         
# Стоит полностью оформить все графики        

# In[35]:


#строим гистограму по всем значениям, удаляем низкие
df.kitchen_area.hist()
df.query("kitchen_area < 5")
df = df.drop(df[df["kitchen_area"] < 4].index)


# In[36]:


df = df.drop(df[df["kitchen_area"] > 40].index)


# In[37]:


#сторим гистограму по всем значениям общей площадью

df.total_area.hist();


# In[38]:


#фильтруем низкие значения
df.query("total_area < 21")
df = df.drop(df[df["total_area"] < 21].index)


# In[39]:


#фильтруем высокие значения
df.query("total_area > 170")
df = df.drop(df[df["total_area"] > 170].index)


# In[40]:


df["parks_nearest"].hist();


# In[41]:


df.query("parks_nearest > 1500")


# In[42]:


df.query("cityCenters_nearest > 50000")


# In[43]:


df["cityCenters_nearest"].hist();


# In[44]:


df.floors_total.hist();


# <div class="alert alert-danger">
# <font size="4"><b>❌ Комментарий ревьюера в4</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />          
# Стоит изменить параметры отображения гистограммы (добавить кол-во корзин), сейчас  трудно определить типовую высотность зданий
#         
# ![image.png](attachment:image.png)        

# In[45]:


df["floor_cat"].hist();


# In[46]:


#cмотрим на минимально низкие значения и первый квантиль
df["last_price"].hist(range=(12000,1500000));


# In[47]:


#удаляем наименее репрезентативные данные
df = df.drop(df[df["last_price"] < 900000].index)


# In[48]:


df["last_price"].hist(range=(6800000,30000000));


# In[49]:


df = df.drop(df[df["last_price"] > 30000000].index)


# In[50]:


df.describe()


# 1. Ceiling_height: На первой гистограме были заменты аномально низкие значения (1м) и высокие (100м). Это отчасти может быть ошибкой, вызванной человеческим фактором. Такие значения были исправлены. Были удалены значения меньше 2.5 метров, тк согласно гос стандартам минимально допустимое значение соотвествует 2.4 м. Были также удалены высокие потолки, выше 4м, тк они являются нерепрезентативными.
# 2. Rooms: На гистограме заметны нестандарные значения. Значения 0 были заменены на 1, тк в квартире должна как минимум быть одна комната. Удаляем высокие и редкие значения, квариры с более чем 8 комнатами.
# 3. Days_exposition: На гистограме заметны нестандарные значения. Были удалены значения с показателями ниже 5 дней, тк они нерепрезентативны, также редкими оказываются значения выше 1100 дней.
# 4. Living_area:  На первой гистограме были заметны аномально низкие значения (2м) и высокие (409м). Cогласно гос стандартам минимальное значение здесь 14 кв. Тк таких данных достаточно много, отсекаем значения с запасом, ниже 11 м. На гистограме также заметно, что квартиры площадью больше 110м редки. Они были удалены.
# 5. Kitchen_area: На первой гистограме были заметны аномально низкие значения (1м) и высокие (112м). Cогласно гос стандартам минимально допустимая площадь кухни не менее 5 м, фильтруем данные менее 4 м. Отсекаем значения выше 40м.
# 6. Total_area: Гистограма показывает наличие нестандартно низкие и высокие значения. Минамальный порог устанавливаем в 21м, опираясь на гос стандрты и распределение данных. Показатели более 170 м согласно гистрограме являются нерепрезентативными.
# 7. Parks_nearest: на гистограме видно, что большинство квартир находится на расстоянии от 400 до 600 метров от парка. Незначительная часть данных находится на расстоянии 15000км и больше, поскольку при анализе данных этот параметр не будет определяющим, отказываемя от фильтрации на этом этапе в пользу сохранения данных.
# 8. Citycenters_nearest: на гистограме видно, что большинство квартир сконцентрировано на участке от 7 до 20 км от центра. Часть данных (менее 1 процента) находится на расстоянии 50000км и больше, удаляем эти данных тк отдаленность от центра будет важным фактором при дальнейшем анализе.
# 9. Floor_cat: Гистограмма показывает, что больше всего квартир представлено в категории "другой", более 16000, на последнем этаже расположены около 3000 квартир, и самая маленькая категория это квартиры на первом этаже, менеее 2500 единиц.
# 10. Last_price. В таблице заменты аномально высокие и низкие значения, строим по них гистограмму (минимальному значению и первому квантилю и максимальному значению и третьему квантилю). Удаляем нерепрезентативные данные.

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера в4</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />  У большей части объявлений нет данных в этой колонке, стоит поправить вывод
#         
#         Parks_nearest: на гистограме видно, что большинство квартир находится на расстоянии от 400 до 600 метров от парка. Незначительная часть данных находится на расстоянии 15000км и больше, поскольку при анализе данных этот параметр не будет определяющим, отказываемя от фильтрации на этом этапе в пользу сохранения данных.

# <div class="alert alert-da nger">
# <font size="4"><b>❌ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />  Гистограммы строятся кодом
#         
#         # check
#         df_check.total_area.hist(bins = 150, figsize = (15,3));
#         
# это пример по сырой выборке, ты рисуешь по своей, можно добавить оформление: название и другие элементы
#         
#         
# Осталось добавить 10 гистограмм и 10 минивыводов
#         
# Шаг 4. Проведите исследовательский анализ данных:
# 1.	Изучите следующие параметры объектов:
#     +	общая площадь;
#     +	жилая площадь;
#     +	площадь кухни;
#     +	цена объекта;
#     +	количество комнат;
#     +	высота потолков;
#    
#     +	тип этажа квартиры («первый», «последний», «другой»);
#     +	общее количество этажей в доме;
#     +	расстояние до центра города в метрах;
#      
#     +	расстояние до ближайшего парка.
#     
# 
# 
# __Постройте отдельные гистограммы для каждого из этих параметров.__ Опишите все ваши наблюдения по параметрам в ячейке с типом markdown.        

#  <div class="alert alert-da nger">
# <font size="4"><b>❌ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />          
# Осталось добавить 10 гистограмм и 10 минивыводов
#         
# Шаг 4. Проведите исследовательский анализ данных:
# 1.	Изучите следующие параметры объектов:
#     +	общая площадь;
#     +	жилая площадь;
#     +	площадь кухни;
#     +	цена объекта;
#     +	количество комнат;
#     +	высота потолков;
#    
#     +	тип этажа квартиры («первый», «последний», «другой»);
#     +	общее количество этажей в доме;
#     +	расстояние до центра города в метрах;
#      
#     +	расстояние до ближайшего парка.
#     
# 
# 
# __Постройте отдельные гистограммы для каждого из этих параметров.__ Опишите все ваши наблюдения по параметрам в ячейке с типом markdown.        

# #### check gap

# In[51]:


df.info()


# In[52]:


# check
data = df.copy()


# In[53]:


df.isna().sum()


# <div class="alert alert-dan ger">
# <font size="4"><b>❌ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
# стоит сменить тип данных в 
#         
#          
#  
#          6   floors_total          21605 non-null  float64      
#         
# здесь пропуски можно удалить, кол-во их минимально ⬆⬆⬆
#         
#         
#          13  balcony               21689 non-null  float64         
#          

# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
# 
# __проверим какие аномалии остались__ таблица ниже

# In[54]:


# check

# Показатели о кол-ве объявлений в датасете, минимальных и максимальных значениях 
# в выбранных параметрах о продаже квартир
# сырые данные

(
    df[['rooms', 'total_area', 'ceiling_height', 'days_exposition', 'last_price', 'living_area',  'kitchen_area',
          'floor', 'floors_total']]
    .apply (['count', 'min', 'max'])   
    .style.format("{:,.2f}")
)


# <div class="alert alert-danger">
# <font size="4"><b>❌ Комментарий ревьюера в4</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Осталась пара странных небоскребов 🤝

# In[55]:


# check
df.hist(column = 'days_exposition', bins = 50, figsize = (15,3), range = (0,5));

df.hist(column = 'days_exposition', bins = 50, figsize = (15,3), range = (0,5))
plt.ylim(0, 40);


# <div class="alert alert-d anger">
# <font size="4"><b>❌ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />остались аномалии и редкости (в т.ч. и хвосты) в колонках: 
#         
#          'ceiling_height', 'days_exposition', 'last_price', 'living_area',  'kitchen_area'
#         
# для определения хвостов, редкостей и аномалий смотрим на минимальные и максимальные значения, строим несколько гистограмм по каждому параметру
#         
# например в таблице мы видим аномалию квартиру за 12 тыс. руб. ..., а на гистограмме редкую скорость продаж в один или два дня
#         
#         
# стоит учесть наличие пропусков при фильтрации данных

# <div class="alert alert-da nger">
# <font size="4"><b>❌ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />остались аномалии и редкости (в т.ч. и хвосты) в колонках: 
#         
#         'rooms', 'total_area', 'ceiling_height', 'days_exposition', 'last_price', 'living_area',  'kitchen_area', 'floors_total'
#         
# стоит обратить внимание на минимальные и максимальные значения в выборке и учесть наличие пропусков при фильтрации данных
#         
# 

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Доп. задание, на твое усмотрение — сможешь добавить в таблицу расчет медианного значения?
#         
#         (
#             data[['rooms', 'total_area', 'ceiling_height', 'days_exposition', 'last_price', 'living_area',  'kitchen_area',
#                   'floor', 'floors_total']]
#             .apply (['count', 'min', 'max','median'])   
#             .style.format("{:,.2f}")
#         )

# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Для выполнения пункта 4.1. (или в старой версии п.2.4) существует два подхода
#         
# Можно механически бороться с выбросами (при помощи межквартильного размаха), ...
#                
# основная проблема такого подхода — не учитывается неоднородность нашей выборки: у нас здесь и малые поселки, и вторая столица страны, и исторический фонд и массовая застройка, и однушки и довольно большое кол-во многокомнатных квартир, или наоборот одна две квартиры с количеством комнат больше 7-ми ...
#         
# 
#         
# если бы у нас в таблице были бы только однокомнатные квартиры из определенного района массовой застройки, тогда да, мы бы боролись с выбросами традиционными способами, при нашем многообразии населенных пунктов, многокомнатности такие подходы не работают... т.е. они работают, но это усложнит наш проект — придется разбить и объединить записи нашей таблицы по нескольким параметрам (кол-во комнат, район, и т.д.), а затем только выполнять все остальные пункты на каждой отдельной выборке
#         
# Остается другой подход — убираем редкие значения и следим за количеством потерь... 
#          
# Для выборки из 23-х тысяч значений, несколько записей со стоимостью квадратного метра выше 1-го млн. руб., довольно редкое явление
# 
# Хороший пример, высота потолков, которую мы отрезаем по нижней и верхней планке, это скорее аномальные записи, посмотрим на другой аспект — на редкости: кол-во комнат
# 
# __т.е. мы не говорим о том, что квартир с кол-ом комнат выше 7 не бывает, мы говорим, что для нашего исследования это редкие выбивающиеся из общей картины уникальные объекты, по которым необходимо проводить отдельную работу ...__
#         
# подобным образом рассматриваем и остальные параметры
#         
# наши помощники
#         
# 1. гистограммы, с хорошим масштабом
# 2. метод describe() или облегченная версия, пример выше
# 3. метод value_counts()
#         
# плюс жизненный опыт 

# In[56]:


# check

try:
    df_check = pd.read_csv('https://code.s3.yandex.net/datasets/real_estate_data.csv', sep='\t')
# если не получилось прочитать файл из локальной папки, то загружаем данные из сети
except:
    df_check = pd.read_csv('real_estate_data.csv', sep='\t')


# In[57]:


# check
df_check.rooms.value_counts().to_frame()
df = df.query('rooms < 8')
df


# In[58]:


# check
df_check.total_area.hist(bins = 150, figsize = (15,3));
#df["total_area"].sort_values().unique()
df = df.query('total_area < 251')
n = (df["rooms"] == 0)
df.loc[n,"rooms"] = 1
df.describe()


# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />т.е. все квартиры менее 20-ти и более 250-ти квадратных метров можно считать редкостями
#        

# In[59]:


# check
df_check.total_area.hist(bins = 150, figsize = (15,3), range = (180,500));


# In[60]:


# check
df_check.total_area.hist(bins = 15, figsize = (15,3), range = (180,500));


# In[61]:


# check
df_check.total_area.hist(bins = 15, figsize = (15,3), range = (0,25));


# <div class="alert alert-dang er">
# <font size="4"><b>❌ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Осталось выполнить пункт 4.1 (в старой версии п.2.4) из брифа проекта
# 
# В некоторых параметрах встречаются редкие и выбивающиеся значения. При построении гистограмм удалите их. Например, в столбце ceiling_height может быть указана высота потолков 25 м и 32 м. Логично предположить, что на самом деле это вещественные значения: 2.5 м и 3.2 м. Попробуйте обработать аномалии в этом и других столбцах, если они есть. Если природа аномалии понятна и данные действительно искажены, то восстановите    корректное значение. В противном случае удалите редкие и выбивающиеся значения. 
#         
# __Критичный уровень потерь записей на этапе предобработки составляет 10%, оптимальный 5%__
#         
# Если при фильтрации одной колонки, на этом проекте, теряем больше одного процента данных от изначального объема, стоит еще раз пересмотреть условия фильтрации        

# In[62]:


# check

# Значения параметров объектов недвижимости на разных квантилях

(
    data[['rooms', 'total_area', 'ceiling_height', 'days_exposition', 'last_price', 'living_area',  
        'kitchen_area', 'floor',   'floors_total']]
    .quantile([0.0012, 0.01, .5, .99, .9988]) # выбираем размах в 0,9976 квантилей 
    .style.format("{:,.2f}")
)


# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Квантили что это такое (первая ссылка иногда не открывается)
#         
# https://fin-accounting.ru/cfa/l1/quantitative/cfa-quartiles-quintiles-deciles-percentiles?ysclid=l7gy2kky4i156375632
#         
# https://www.codecamp.ru/blog/percentile-vs-quartile-vs-quantile/?ysclid=lg89wjm4zz267333250        
#         
# они помогают увидеть редкости и аномалии в данных

# # example 1

# #### example 3

# ##### example 4

# <div style="border:solid steelblue 3px; padding: 20px">
# <font size="4">🍕<b> Комментарий ревьюера</b></font>
# <br /> 
# <font size="3", color = "black">
# <br />
# Стоит выделять разделы проекта заголовками разного уровня, за уровень отвечает количество знаков #
#     
#         # example 1
# 
#         #### example 3
# 
#         ##### example 4
#     
# Пожалуйста, воспользуйся методичкой по оформлению проектов. Ее можно найти в блоке курса: Полезные инструкции для учёбы - Оформление проекта - Рекомендации по выполнению проектов    

# ### 4.2

# In[63]:


#2.формируем данные по скорости продажи по местам с наибольшим количеством данных
x = df.groupby("locality_name")["days_exposition"].count().sort_values(ascending=False).head(10)
filtered_x = df.query("locality_name.isin(@x.index)")
filtered_x 


# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Интересное исследование, молодец

# In[64]:


for a, b in filtered_x.groupby("locality_name"):
    b.plot(y="days_exposition",title=a,style="o")


# In[65]:


#удаляем аномально высокие значения для каждой локации
filtered_x = filtered_x.drop(filtered_x[(filtered_x["locality_name"] == "Всеволожск") & (filtered_x["days_exposition"] > 800)].index)
filtered_x = filtered_x.drop(filtered_x[(filtered_x["locality_name"] == "Выборг") & (filtered_x["days_exposition"] > 600)].index)
filtered_x = filtered_x.drop(filtered_x[(filtered_x["locality_name"] == "Гатчина") & (filtered_x["days_exposition"] > 600)].index)
filtered_x = filtered_x.drop(filtered_x[(filtered_x["locality_name"] == "Колпино") & (filtered_x["days_exposition"] > 500)].index)
filtered_x = filtered_x.drop(filtered_x[(filtered_x["locality_name"] == "Кудрово") & (filtered_x["days_exposition"] > 599)].index)
filtered_x = filtered_x.drop(filtered_x[(filtered_x["locality_name"] == "Мурино") & (filtered_x["days_exposition"] > 500)].index)
filtered_x = filtered_x.drop(filtered_x[(filtered_x["locality_name"] == "Парголово") & (filtered_x["days_exposition"] > 500)].index)
filtered_x = filtered_x.drop(filtered_x[(filtered_x["locality_name"] == "Пушкин") & (filtered_x["days_exposition"] > 599)].index)
filtered_x = filtered_x.drop(filtered_x[(filtered_x["locality_name"] == "Санкт-Петербург") & (filtered_x["days_exposition"] > 1200)].index)
filtered_x = filtered_x.drop(filtered_x[(filtered_x["locality_name"] == "Шушары") & (filtered_x["days_exposition"] > 500)].index)


# In[66]:


#проверяем на моды
filtered_x['days_exposition'].value_counts().to_frame().head(20).plot(kind = 'barh', figsize = (15,6), rot = 0);
filtered_x


# In[67]:


#удаляем моды
filtered_x1 = filtered_x.drop(filtered_x[(filtered_x["days_exposition"] == 45) | (filtered_x["days_exposition"] == 60)].index);
filtered_x1['days_exposition'].value_counts().to_frame().head(20).plot(kind = 'barh', figsize = (15,6), rot = 0);


# In[68]:


#строим таблицу по всем данным
filtered_table = filtered_x.pivot_table(index="locality_name",values="days_exposition",aggfunc=["median","mean"])
filtered_table.columns = ["days_median","days_mean"]
filtered_table = filtered_table.reset_index()
filtered_table["days_mean"] = filtered_table["days_mean"].astype(float).round()
filtered_table.index = np.arange(1, len(filtered_table)+1)
print(filtered_table);

filtered_table.plot(x="locality_name",y=["days_median","days_mean"],figsize=(15, 5), xlim=[0,9], ylim=[50,200],title="Exposition_per_location");


# In[69]:


#строим таблицу по данным без модов
filtered_table1 = filtered_x1.pivot_table(index="locality_name",values="days_exposition",aggfunc=["median","mean"])
filtered_table1.columns = ["days_median","days_mean"]
filtered_table1 = filtered_table1.reset_index()
filtered_table1["days_mean"] = filtered_table1["days_mean"].astype(float).round()
filtered_table1.index = np.arange(1, len(filtered_table1)+1)
print(filtered_table1);

filtered_table1.plot(x="locality_name",y=["days_median","days_mean"],figsize=(15, 5), xlim=[0,9], ylim=[50,200],title="Exposition_per_location");


# In[70]:


#видим большую разницу,приводим моды к стандартным значениям, 
#предположим, что 45 и 60 действительно были накручены, но так как с точностью
#мы это сказать не можем, произвольно удалим 70 процентов данных,
#чтобы привести их к средним показателям по другим квартирам


# In[71]:


filtered_x["days_exposition"].mean().round(1)


# In[72]:


b = filtered_x.query("days_exposition == 45").head(320)
c = filtered_x.query("days_exposition == 60").head(320)
idxs = list(b.index.values) 
idxs_c = list(c.index.values)
filtered_x.drop(idxs_c,axis=0,inplace=True)
filtered_x.drop(idxs,axis=0,inplace=True)


# In[73]:


filtered_x['days_exposition'].value_counts().to_frame().head(20).plot(kind = 'barh', figsize = (15,6), rot = 0);


# In[74]:


#строим таблицу с медианным данным в модах
filtered_table2 = filtered_x.pivot_table(index="locality_name",values="days_exposition",aggfunc=["median","mean","max"])
filtered_table2.columns = ["days_median","days_mean","max"]
filtered_table2 = filtered_table2.reset_index()
filtered_table2["days_mean"] = filtered_table2["days_mean"].astype(float).round()
filtered_table2.index = np.arange(1, len(filtered_table1)+1)
print(filtered_table2);
#filtered_table2.boxplot("days_exposition")
filtered_x.boxplot(column=["days_exposition"],by="locality_name",figsize=(15, 10))

filtered_table2.plot(x="locality_name",y=["days_median","days_mean"],figsize=(15, 5), xlim=[0,9], ylim=[50,200],title="Exposition_per_location",grid=True);


# <div class="alert alert-dang er">
# <font size="4"><b>❌ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />          
# Осталось добавить выводы под каждый параметр
#         
# Шаг 4. Проведите исследовательский анализ данных:
#         
# 2. Изучите, как быстро продавались квартиры (столбец days_exposition). Этот параметр показывает, сколько дней было размещено каждое объявление.
# + Постройте гистограмму.
# + Посчитайте среднее и медиану.
#         
# В ячейке типа markdown опишите, сколько времени обычно занимает продажа. Какие продажи можно считать быстрыми, а какие — необычно долгими?

# Вывод.
# На графике обозначены как медианные, так и средние значения. Ориентироваться однако будем на медианные, поскольку разница в этих показателях значительна, что свидетельствует о большом разбросе данных. Об этом свидетельствуют и максимальные показатели скорости продажи.
# 
# На графике видно, что быстрее всего квартиры продаются в Кудрово, медианное значение здесь 74 дня, среднее 126, медленными можно считать продажи более 175 дней (3 квантиль), аномально долгими более 350 дней. Быстрыми можно считать продажи занимающие меньше 50 дней (первый квантиль).
# 
# В Всеволожске квартиры согласно полученным данным продаются медленне всего, медианное значение 127 дней, быстрые продажи занимают 45 дней и меньше. Медленные 250 дней.
# 
# Исходя из данных таблицы и графика можно сделать вывод, что быстрыми для всех населенных пунктов считаются продажи в 45 дней и меньше. Медленными можно считать продажи занимающие 190 дней и дольше.
# 

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
#         
# __Интересно посмотреть на изменение средней  скорости продаж по годам__
#         
# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ответ в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
#         done

# In[75]:


#строим график динамики по годам для каждой локации
locality = filtered_x["locality_name"].unique()
for a in locality:
    x2 = filtered_x.where(filtered_x["locality_name"] == a)
    x2.pivot_table(index="year",values="days_exposition",aggfunc=["mean","median"]).plot(kind="line",title=a,xticks=[2015,2016,2017,2018,2019],xlim=(2015,2019))     
plt.show()
    
    


# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Все верно, скорость продаж уменьшается, квартиры продаются быстрее. Только использовать с осторожностью, у нас еще больше 3000 непроданных квартир, которых нет в статистике о средней скорости продаж

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />         
# Не исследованы моды (пиковые значения) в 'days_exposition' и как они влияют на скорость продажи, подсказка на что смотреть
#         
# [Условия размещения объявлений](https://yandex.ru/support/realty/owner/home/add-ads-housing.html)
#         
# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ответ в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# попыталась реабилитироваться, предварительно отфильтровав данные

# In[76]:


# check
# Моды на сырых данных
 
df_check['days_exposition'].value_counts().to_frame().head(20).plot(kind = 'barh', figsize = (15,6), rot = 0);


# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Моды на сырых данных
#         
#         Мода (Mo) представляет собой значение изучаемого признака, повторяющееся с наибольшей частотой, т.е. мода – значение признака, встречающееся чаще всего. Медианой (Me) называется значение признака, приходящееся на середину ранжированной (упорядоченной) совокупности, т.е. медиана – центральное значение вариационного ряда.
#         
# Выделяются моды на 45 и 60 дней, а значения на 44 и 45 дней, явно имеет техническую причину снятия, из-за формата числа 
#         
# В нашем проекте — моды, из-за подозрения что это техническое снятие с продаж, могут искажать реальный расчет скорости продажи квартиры
#         
# второе предположение о причине появления подобных значений — результат деятельности роботов агентств недвижимости, которые обновляют свои предложения с определенной частотой        
#         
# полностью из проекта удалять их не стоит, можно временно исключить из расчета скорости продаж

# ### 4.3

# In[77]:


df.plot.scatter(x="total_area",y="last_price")
plt.show()
df["last_price"].corr(df["total_area"]).round(1)


# In[78]:


df.plot.scatter(x="living_area",y="last_price")
plt.show()
df["last_price"].corr(df["living_area"]).round(1)


# In[79]:


df.plot.scatter(x="kitchen_area",y="last_price")
plt.show()
df["kitchen_area"] = df["kitchen_area"].astype("float32")
df["last_price"].corr(df["kitchen_area"]).round(1)


# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Почему мы не применяем группировку данных для диаграмм рассеяния.
#         
# Дело в качестве графика. Если мы сводим данные в таблицу — точечный график не покажет всех нюансов в данных, например выбросы - отдельные точки, или отдельные облака
#         
# Пример из датасета про цветы - Ирисы ⬇⬇, три класса Ирисов отличаются по ширине и длине околоцветника, что прекрасно можно наблюдать на точечной диаграмме. Если мы построим сводную таблицу и усредним значения, мы этого разделения не увидим
#         
# ![image.png](attachment:image.png)        

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Стоит перерисовать первые три графика без применения группировки
#         
# ![image.png](attachment:image.png)        
#         
# Можно попробовать настроить вид точечных графиков      
#     
# [Как сделать диаграмму рассеяния из фрейма данных Pandas](https://www.codecamp.ru/blog/pandas-scatter-plot/?ysclid=lh0tbpkoa9628147030)
#     
# Примеры расчета коэф. корреляции и не только
#         
# [Исследуем отношение между переменными](https://dfedorov.spb.ru/pandas/downey/%D0%98%D1%81%D1%81%D0%BB%D0%B5%D0%B4%D1%83%D0%B5%D0%BC%20%D0%BE%D1%82%D0%BD%D0%BE%D1%88%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BC%D0%B5%D0%B6%D0%B4%D1%83%20%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D0%BC%D0%B8.html?ysclid=l9ev0utyg728177057)     
#         
# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Перестроила графики (выше) без группировки

# In[80]:


df.groupby("rooms")["last_price"].median().plot()
plt.show()

df["last_price"].corr(df["rooms"]).round(1)


# In[81]:


df.pivot_table(index="year",columns="floor_cat",values=["last_price"],aggfunc="count").plot();


# In[82]:


df.groupby("year")["total_area"].median().plot(xticks=[2015, 2016, 2017, 2018, 2019],xlim=(2015,2019));


# In[83]:


df.groupby("year")["last_price"].median().plot(xticks=[2015, 2016, 2017, 2018, 2019],xlim=(2015,2019));
df.groupby("year")["last_price"].median()


# In[84]:


df.groupby("year")["last_price"].count().plot(xticks=[2015, 2016, 2017, 2018, 2019],xlim=(2015,2019));


# <div class="alert alert-dan ger">
# <font size="4"><b>❌ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
# Чтобы объяснить причину — почему вместо роста средней цены  на нашем графике мы наблюдаем снижение с 2014 года, и только в 2019 году небольшое повышение цен, когда реальный рынок растет из года в год, нам потребуются две таблицы или графика (на твое усмотрение)     
#         
#         
#         Стоит дополнить  вывод об изменении цен по годам, необходимо учесть другие факторы, которые также изменяются с годами: площадь и кол-во объявлений о продаже (стоит добавить или графики, или сводные таблицы и исследовать взаимное влияние параметров)
#         
# Берем твой пример
#         
#         df.groupby("year")["last_price"].median()
#         
# для первой таблицы стоит в параметре 'last_price' заменить цену на общую площадь
#         
# вторую таблицу с кол-вом объявлений ты уже сделала
#         
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot_table.html?highlight=pivot_tab#pandas.DataFrame.pivot_table
#         
# [Подробное руководство по группировке и агрегированию с помощью pandas](https://dfedorov.spb.ru/pandas/%D0%9F%D0%BE%D0%B4%D1%80%D0%BE%D0%B1%D0%BD%D0%BE%D0%B5%20%D1%80%D1%83%D0%BA%D0%BE%D0%B2%D0%BE%D0%B4%D1%81%D1%82%D0%B2%D0%BE%20%D0%BF%D0%BE%20%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B5%20%D0%B8%20%D0%B0%D0%B3%D1%80%D0%B5%D0%B3%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8E%20%D1%81%20%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E%20pandas.html)
#         
# затем берем три графика или таблицы вместе и находим причину падения средних цен с 2014 по 2019 год
#         
#         

# <div class="alert alert-da nger">
# <font size="4"><b>❌ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Стоит дополнить  вывод об изменении цен по годам, необходимо учесть другие факторы, которые также изменяются с годами: площадь и кол-во объявлений о продаже (стоит добавить или графики, или сводные таблицы и исследовать взаимное влияние параметров: кол-во записей и изменение средней цены и средней площади в течение лет)
#         
#         в этом пункте самое главное создать таблицы с сгруппированнами данными, при помощи группировки или сводных таблиц

# 

# In[85]:


df.groupby("month")["last_price"].median().plot()
plt.show()


# In[86]:


df.groupby("week_day")["last_price"].median().plot()
plt.show()


# In[87]:


df.groupby("week_day")["last_price"].mean().plot()
plt.show()


# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> на проектах стоит снижать размерность выводимой информации, где не требуется максимальная точность, до одного или двух знаков после запятой
#         
#         0.5665437762676155

# <div class="alert alert-dan ger">
# <font size="4"><b>❌ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Стоит  добавить промежуточный вывод для подраздела о поиске зависимостей

# Вывод.
# На графике заметна зависимость цены от общей площади, кроме того корреляция составляет 0.8, корреляция по жилой площади равна 0.7, зависимость от площади кухни равно 0.6.
# 
# На графике видна зависимость цены от количества комнат. Корреляция составляет 0.5. 
# 
# Дешевле всего квартиры на первом этаже, на последнем этаже средняя стоимость 43 миллиона дороже всего квартиры ни на первом, ни на последнем этаже.
# 
# Дороже всего квартиры, выставленные на продажу в апреле, применять корреляцию здесь неэффективно. На графике видно, что дороже квартиры выставляющие на продажу в понедельник применять корреляцию здесь неэффективно.
# 
# На графике заметна тенденция на снижение цен в период с 2016 по 2018, что не характерно для рынка в целом.
# Чтобы исследовать аномалию была установлена репрезентативность данных. 
# 
# На 2017 год пришлось 7768 квартир, а в 2018 год 8084, в то время как на 2016 - 2624, а в 2019 - 2722. Если мы изолированно посмотрим на сопоставимые по количеству данных года, то здесь заметна позитивная динамика, медианная цена в 2016 составила 4480000, в 2019 - 5000000.
#  
# В то же время в 2014, по которому данных меньше всего 6950000, то есть самая высокая, можно предположить, что резкое снижение цен в 2017, 2018 связано с различием в количестве данных.
# 
# Также был построен график по медианной площади, здесь не наблюдается очевидной корреляции между снижением медианой площади и снижением цены. Поэтому площадь скорее нельзя считать значительным фактором, объясняющим снижение цен в период с 2016 по 2018 года. Cкорее всего, снижение цен связно с резким повышением количества квартир в 2017,2018 года на рынке. Чем больше предложение, тем меньше цены. 
# 
# 

# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера в4</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
#         
# Если смотреть только на изменение средней или медианной цены по годам мы можем сделать некорректный вывод, что цены падали, а на самом деле цена это параметр на который влияет несколько других факторов, по этой причине можно посмотреть на основные из них: 
#         
# + изменение кол-ва записей — принять решение о достаточности данных для анализа и сравнения (сравнивать 100 объявлений и 8000, а возможно, что они еще и из разных локаций, не совсем корректно) 
# + изменение площади, как основного параметра от которого зависит стоимость квартиры, в 2017-2018 гг. на сервис или рынок ИТ-торговли недвижимостью пришел массовый продавец, и средние значения площади упали ..., а за ней и цена
# + изменение кол-ва поданных объявлений из разных локаций, т.к. есть питерские квартиры, а есть выборгские квартиры и стоят они по разному, и в разные годы могло быть больше квартир из определенной локации
# + полнота периода для анализа, 2014 и 2019 гг. неполные, а у нас есть сезонные колебания цен, например летнее снижение цен
# 
# и т.д.

# ### 4.4
# 
# Поставьте 'x' в выполненных пунктах. Далее нажмите Shift+Enter.

# In[88]:


#4. 10 самых популярных пунктов 
# cоздаем список с наибольшим массивом данных
top_10 = df.groupby("locality_name")["rooms"].count().sort_values(ascending=False).head(10)
# cоздаем датафрейм с наибольшим массивом данных
filtered_top = df[df['locality_name'].isin(top_10.index)]
# считаем медианну по этим данным
filtered_top = filtered_top.groupby("locality_name")["price"].median().sort_values(ascending=False)
filtered_top.plot(kind="barh");
filtered_top


# Был сформирован топ 10 населенных пунктов по количеству данных и посчитаны медианные показатели цена за кв. метр. Самые дорогой кв метр в Петербурге, 104072.40. Cамый дешевый в Выборг, 58407.080.

# <div style="border:solid steelblue 3px; padding: 20px">
# <font size="4">🍕<b> Комментарий ревьюера в3</b></font>
# <br /> 
# <font size="3", color = "black">
# <br />      Можно развернуть график
#     
#      kind='barh'

# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />ТОП-10 рассчитан корректно

# <div class="alert alert-dange r">
# <font size="4"><b>❌ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
# Недостаточно найти числа, стоит их показать красиво, удобно и наглядно, чтобы одного взгляда хватило, где самые самые, а где подешевле 📊
#         <div class="alert alert-danger">
# <font size="4"><b>ответ в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
# построила гистограмму

# <div style="border:solid steelblue 3px; padding: 20px">
# <font size="4">🍕<b> Комментарий ревьюера в2</b></font>
# <br /> 
# <font size="3", color = "black">
# <br />         
#     
# [Постер поможет выбирать вид графиков](https://www.notion.so/6c5ae8ceb8b5411e907c93c9b5e6a44e)

# ### 4.5

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> не стоит за счет комментариев увеличивать ширину строки ⬇⬇⬇

# In[89]:


#объединяем данные по 0 и 1 км о центра в одну категория
#для cохранения выборки в 1 км, иначе ее придется удалить, однако она является
#важной для исследования и наглядности данных

sp_stat = df.query("locality_name == 'Санкт-Петербург'")
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    sp_stat_2 = (sp_stat["to_center"] == 0)
    sp_stat.loc[sp_stat_2,"to_center"] = 1


# In[90]:


#5.Выделите квартиры в Санкт-Петербурге с помощью столбца locality_name и 
#вычислите их среднюю стоимость на разном удалении от центра»:
# cоздаем датафрейм для Петербурга
#sp_stat = df.query("locality_name == 'Санкт-Петербург'")
#sp_stat.groupby("to_center")["last_price"].count().plot(kind="bar");
n = sp_stat.pivot_table(index=["to_center"],values="last_price",aggfunc=["mean","count"])
n.columns = ["mean","count"]
n.reset_index(inplace=True)
print(n)
#видим, что данные распределены неравномерно, добавляем столбец count в таблицу
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    for a in n["to_center"]:
        sp_stat.loc[(sp_stat['to_center'] == a),'count'] =         sp_stat.loc[(sp_stat["to_center"] == a),"last_price"].count()
# по новому столбцу фильтруем данные, оставляем те, где строк больше 200
sp_stat = sp_stat.drop(sp_stat[sp_stat['count'] < 200].index)


# In[91]:


e = sp_stat.pivot_table(index=["to_center","rooms","year"],values="last_price",aggfunc="mean")
e


# In[92]:


# видим,что данных мало по 2014, удаляем их из датасета
sp_stat.groupby("year")["last_price"].count()


# In[93]:


#также мало информации по 5 и 6 комнатным квартирам
sp_stat.groupby("rooms")["last_price"].count()


# In[94]:


#удаляем нерепрезентативные данные их датасета
sp_stat = sp_stat.drop(sp_stat[sp_stat['year'] == 2014].index)


# In[95]:


#удаляем нерепрезентативные данные их датасета
sp_stat = sp_stat.drop(sp_stat[sp_stat['rooms'] > 4].index)


# <div class="alert alert-dan ger">
# <font size="4"><b>❌ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Стоит  оставить 4-х комнатные это около 5-6% данных

# In[96]:


sp_stat.pivot_table(index="to_center",columns="rooms",values="last_price",aggfunc="median").plot(title="median_price");


# In[97]:


sp_stat.pivot_table(index="to_center",columns="rooms",values="last_price",aggfunc="count").plot(title="rooms");


# In[98]:


sp_stat.pivot_table(index="to_center",columns="floor_cat",values="last_price",aggfunc="count").plot(title="floor_category");


# In[99]:


stat = sp_stat.query("rooms == 4")
stat.pivot_table(index="to_center",columns="rooms",values="total_area",aggfunc="median").plot(kind="line",title="total_area, 4 rooms");    
plt.show()


# На первом графике, где показана цена недвижимости в зависимость от отдаленности от центра города для 4 категорий квартир: 1-комнатных, 2-комнатных, 3-комнатных и 4-комнатных, наблюдается ожидаемая корреляция зависимости цены от близости к центру. Такая тенденция прослеживается для 1, 2, 3-комнатных квартир начиная с 4 километров. Однако квартиры на первых 3 километрах дешевле, чем квартиры на 4 километре. Кроме того, аномалии заметны и для 4 комнатных квартир, они резко дорожают на 8 километре. Сильный спад наблюдается на 12 километре.
# 
# Для дальнейшего анализа строим два графика: 1. Количество 1,2,3,4 комнат на каждом километре. 2. Количество квартир на первом, последнем и других этажах на каждом километре. 
# 
# На втором графике видим, что на отрезке от 1 до 3 км, в целом представлена меньше данных, второй график показывает, что на этом отрезке также  наименьшая концентрация квартир категории «другой» по параметру этаже, а это самая интересная категория квартир. Так же оба графика показывают резкий скачок по общему количеству квартир и большой прирост квартир из категории «другой». Это однако не объясняет аномалии с 4 комнатными квартирами. 
# 
# Cтроим еще один график, теперь только по 4 комнаты квартирам, проверяем общую площадь квартир. Замечаем пик на отметке 8 км и резкий спад на отметке 12 км.
# 
# Можно сделать общий вывод, что за исключением рассмотренных аномалий, наблюдается корреляция цены и отдаленности от центра: чем дальше от центра, тем бюджетнее недвижимость.

# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера в4</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Размер доли категорий квартир с более дешевой стоимостью намного больше на 3-м километре, чем на пятом, что является одной из причин падения и пика...
#         
# возможно к этому фактору добавляются и другие

# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера в4</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Для оптимизации кода расчета доли таких квартир стоит обратить внимание на пример из статьи
#         
#         Работа с групповыми объектами
#         После группировки и агрегирования данных вы можете выполнять дополнительные вычисления для сгруппированных объектов.
# 
#         В следующем примере определим, какой процент от общего количества проданных билетов можно отнести к каждой комбинации embark_town и class.
# 
#         Мы используем метод assign() и лямбда-функцию для добавления столбца pct_total:
# 
#         df.groupby(['embark_town', 'class']).agg({'fare': 'sum'}).assign(pct_total=lambda x: x / x.sum())        
#         
#         
# [Подробное руководство по группировке и агрегированию с помощью pandas](https://dfedorov.spb.ru/pandas/%D0%9F%D0%BE%D0%B4%D1%80%D0%BE%D0%B1%D0%BD%D0%BE%D0%B5%20%D1%80%D1%83%D0%BA%D0%BE%D0%B2%D0%BE%D0%B4%D1%81%D1%82%D0%B2%D0%BE%20%D0%BF%D0%BE%20%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B5%20%D0%B8%20%D0%B0%D0%B3%D1%80%D0%B5%D0%B3%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8E%20%D1%81%20%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E%20pandas.html)

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
# Молодец, у тебя получилось сгруппировать и построить график изменения медианной цены в зависимости от расстояния до центра
#         
# по проекту ищем изменение средней цены за всю квартиру, а не кв. метра

# In[100]:


# check
n.iloc[:,1].plot.bar(rot=0, figsize=(15,5));


# ![image.png](attachment:image.png)

# <div class="alert alert-dang er">
# <font size="4"><b>❌ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />    Для решения задачи 
#         
#     Стоит посмотреть на количество квартир разных категорий (первый, последний, другой), которые продаются на 3-м км. и 5-ом ... и какую долю они занимают на каждом километре, чтобы объяснить пик  и провал в центре
#         
# стоит выполнить группировку данных на питерских квартирах и подсчитать кол-во
#         
# ссылку на статью дублирую (в статье обратить внимание на примеры с двойным индексом)
#         
# [Сводная таблица в pandas](https://dfedorov.spb.ru/pandas/%D0%A1%D0%B2%D0%BE%D0%B4%D0%BD%D0%B0%D1%8F%20%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0%20%D0%B2%20pandas.html?ysclid=lje9wz2vfc28794921)   

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
# Стоит исключить предупреждения. Иногда их бывает слишком много, поэтому важно уметь их скрывать. В этом тебе поможет библиотека warnings. Попробуй найти подходящий метод и убрать предупреждения. 
#         
#         /tmp/ipykernel_245/1202183187.py:5: SettingWithCopyWarning: 
#         A value is trying to be set on a copy of a slice from a DataFrame.
#         Try using .loc[row_indexer,col_indexer] = value instead ...

# ## Шаг 5. Напишите общий вывод

# 1. Используем метод describe для первичного анализа данных. Видим, что для общей площади средний показатель 60 кв, мин значение 12 кв, максимальное 900. Для жилой площади среднее 34 кв, мин значение подозрительно низкое 2кв, максимальное 409 для площади кухни среднее значение 10 кв, мин 1 (также подозрительно низкое),максимальное 112 .Cредняя цена 7 миллионов, мин 121 тысяча, максимальная 760 миллионов. Комнат в среднем 2, мин значение, максимальное 19. Cредняя высота потолков 2,7, мин 1, максимальная 14. Общее количество этажей в доме 5 (учитывая большой разброс показатель mean здесь не репрезентативен,),мин 1, мак 33. Cредняя раcстояние до центра 14 км(учитывая большой разброс показатель mean здесь не репрезентативен),мин равно 0, мак почти 66 км. Cредняя раcстояние до ближайшего парка равно 490м.с огромным значением отклонения, мин 1, максимальное 3190 км. Подобные аномалии были устарены с помощью фильтрации. 
# 
# 2. Были изучены 10 населенных пунктов с большим количеством по показателю быстроты продажи недвижимости. Были установлены медианные значения и построен график, где видны нижние и верхние границы этого показателя. В Санкт-Петербурге медианное значение равно 99 дням. Медленными можно считать продажи от 220 дней, быстрыми менее 30 дней. Исходя из данных таблицы и графика можно сделать вывод, что быстрыми для всех населенных пунктов считаются продажи в 45 дней и меньше. Медленными можно считать продажи занимающие 190 дней и дольше.
# 
# 3. Также был проведен анализ зависимости стоимости недвижимости от различных показателей было установлено, что больше всего на стоимость влияет общая и жилая площадь, площадь кухни. Более слабое влияние также оказывает количество комнат. Четкой зависимости от года публикации месяца или дня установлено не было.
# 
# 4. Согласно первичному анализу, были выявлены расположения с наибольшим количеством данных. Были проанализированы цены на квадратный метр в населенных пунктах. Самая дорогая недвижимость в Санкт-Петербурге, самая дешевая в поселке Выборг.
# 
# 5. Также был проведен анализ по недвижимости в Санкт-Петербурге и влиянии расположение на стоимость недвижимости. Для этого сначала был проведен анализ репрезентативность данных. Порогом была выбрана отметка в 4 процента от общей массы данных. Таким образом были построены 4 графика с репрезентативными данными и всеми данными стоимости недвижимости по километрам. На графике с репрезентативными данными видна более четкая зависимость удаление от центра и цены. Вырисовывается общая тенденция: чем дальше недвижимость расположена от центра, тем она дешевле.
# 
# 

# ### check

# <div class="alert alert-danger">
# <font size="4"><b>❌ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Технически вывод хороший, есть сравнения показателей, инсайты, анализ рынка недвижимости, молодец
#         
# Осталось перепроверить итоговый вывод после исправления всех комментариев

# <div class="alert alert-success">
# <font size="5", color= "seagreen"><b>✔️ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />    
# Выполнила исследовательскую работу, молодец
#         
# Критические ❌ комментарии
# 
#         
# + проверить корректность смены типа данных     
# + сменить тип данных
# + добавить гистограммы в п.4.1         
# + настроить фильтрацию редких значений 
# + добавить вывод в раздел о скорости продаж         
# + добавить вывод в п. 4.3
# + добавить график в ТОП-10
# + исследовать аномалию в п.4.5
# + поправить итоговый вывод
#            
#         
#         
# С ними важно поработать и исправить
#         
# Стоит обратить внимание и на такие комментарии ⚠️
#         
# Если будут вопросы про мои комментарии - задавай, если какой-то формат взаимодействия не устраивает или есть какие-то другие пожелания - пиши :)
# 
# <div class="alert alert-success">
#     <font size="5"><b>Жду твой проект и твои комментарии 🤝</b></font><br />
#     
# нумерация пунктов из брифа проекта, у тебя они могут быть другие
#     
# если не заметил твоих вопросов, просьба выделить цветом    
#     
#     
# __Для успешного исправления комментариев стоит прочитать справочные материалы ⬇⬇⬇__     

# <div style="border:solid steelblue 3px; padding: 20px">
# <font size="4">🍕<b> Комментарий ревьюера в2</b></font>
# <br /> 
# <font size="3", color = "black">
# <br />    
#     
# [Обработка пропусков в данных](https://loginom.ru/blog/missing)
#      
#         
# [Подробное руководство по группировке и агрегированию с помощью pandas](https://dfedorov.spb.ru/pandas/%D0%9F%D0%BE%D0%B4%D1%80%D0%BE%D0%B1%D0%BD%D0%BE%D0%B5%20%D1%80%D1%83%D0%BA%D0%BE%D0%B2%D0%BE%D0%B4%D1%81%D1%82%D0%B2%D0%BE%20%D0%BF%D0%BE%20%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B5%20%D0%B8%20%D0%B0%D0%B3%D1%80%D0%B5%D0%B3%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8E%20%D1%81%20%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E%20pandas.html)
#     
# [Сводная таблица в pandas](https://dfedorov.spb.ru/pandas/%D0%A1%D0%B2%D0%BE%D0%B4%D0%BD%D0%B0%D1%8F%20%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0%20%D0%B2%20pandas.html?ysclid=lje9wz2vfc28794921)
#         
# [Понимание функции transform в Pandas](https://dfedorov.spb.ru/pandas/%D0%9F%D0%BE%D0%BD%D0%B8%D0%BC%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8%20transform%20%D0%B2%20Pandas.html)
#     
# [Как выбрать определенные столбцы из DataFrame](https://dfedorov.spb.ru/pandas/03.%20%D0%9A%D0%B0%D0%BA%20%D0%B2%D1%8B%D0%B1%D1%80%D0%B0%D1%82%D1%8C%20%D0%BF%D0%BE%D0%B4%D0%BC%D0%BD%D0%BE%D0%B6%D0%B5%D1%81%D1%82%D0%B2%D0%BE%20%D0%B8%D0%B7%20DataFrame_.html?ysclid=l9sps5lt6g576766938)
#     
# [How to visualise data using histograms in Pandas](https://practicaldatascience.co.uk/data-science/how-to-visualise-data-using-histograms-in-pandas)
#     
# [8 способов фильтрации фреймов данных Pandas](https://questu.ru/articles/85248/)    

# ## Бонус

# <div style="border:solid steelblue 3px; padding: 20px">
# <font size="4">🍕<b> Комментарий ревьюера в4</b></font>
# <br /> 
# <font size="3", color = "black">
# <br />Диаграмма рассеяния

# In[101]:


# check
import seaborn as sns
import matplotlib.pyplot as plt


# In[102]:


data = df.copy()


# In[103]:


# check
sns.pairplot(data[['last_price', 'total_area', 'rooms', 'cityCenters_nearest']])
plt.gcf().set_size_inches(12,12);


# In[104]:


# check
data[data['rooms'] == 3].query('total_area < 201 and last_price < 25_000_000').plot(kind='scatter',
        y='last_price' , x='total_area', alpha=0.5, subplots=True, figsize=(15,8), c = 'b', s = 4)
plt.title('Диаграмма рассеяния — Общая площадь — цена трешки')


data[data['rooms'] == 3].query('total_area < 201 and last_price < 25_000_000').plot(kind='scatter', 
        y='last_price' , x='living_area', alpha=0.5, figsize=(15,8), c = 'r', s = 4)
plt.title('Диаграмма рассеяния — Жилая площадь — цена трешки');


# In[105]:


# check
data[data['rooms'] == 3].query('total_area < 201 and last_price < 25_000_000').plot(kind='scatter',
        y='living_area' , x='total_area', alpha=0.5, subplots=True, figsize=(15,8), c = 'MediumSpringGreen', s = 4)
plt.title('Диаграмма рассеяния — Общая площадь — Жилая');


# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера в4</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />пример с двойной сортировкой, у меня пример с общей стоимостью

# In[106]:


# check TOP-10
# способы группировки и сортировки информации

(
    data
    .groupby('locality_name')['last_price']
    .agg({'count', 'mean'})
    .sort_values(by = 'count', ascending = False)
    .head(10)
    
).sort_values(by = 'mean', ascending = False).style.format("{:,.0f}")

# .plot(y = 'mean', kind = 'bar')
# стайл и плот вместе не работают


# 

# - [x]  Файл с данными открыт.
#     - [
# []  Файл с данными изучен: выведены первые строки, использован метод `info()`, построены гистограммы.
# - [ ]  Найдены пропущенные значения.
# - [ ]  Пропущенные значения заполнены там, где это возможно.
# - [ ]  Объяснено, какие пропущенные значения обнаружены.
# - [ ]  В каждом столбце установлен корректный тип данных.
# - [ ]  Объяснено, в каких столбцах изменён тип данных и почему.
# - [ ]  Устранены неявные дубликаты в названиях населённых пунктов.
# - [ ]  Обработаны редкие и выбивающиеся значения (аномалии).
# - [ ]  В таблицу добавлены новые параметры:
#        – цена одного квадратного метра;
#        – день публикации объявления (0 - понедельник, 1 - вторник и т. д.);
#        – месяц публикации объявления;
#        – год публикации объявления;
#        – тип этажа квартиры (значения — «первый», «последний», «другой»);
#        – расстояние до центра города в километрах.
# - [ ]  Изучены и описаны параметры:
#         - общая площадь;
#         - жилая площадь;
#         - площадь кухни;
#         - цена объекта;
#         - количество комнат;
#         - высота потолков;
#         - тип этажа квартиры («первый», «последний», «другой»);
#         - общее количество этажей в доме;
#         - расстояние до центра города в метрах;
#         - расстояние до ближайшего парка.
# - [ ]  Выполнено задание «Изучите, как быстро продавались квартиры (столбец `days_exposition`)»:
#     - построена гистограмма;
#     - рассчитаны среднее и медиана;
#     - описано, сколько обычно занимает продажа и указано, какие продажи можно считать быстрыми, а какие — необычно долгими.
# - [ ]  Выполнено задание «Определите факторы, которые больше всего влияют на общую (полную) стоимость объекта». Построены графики, которые показывают зависимость цены от параметров:
#         - общая площадь;
#         - жилая площадь;
#         - площадь кухни;
#         - количество комнат;
#         - тип этажа, на котором расположена квартира (первый, последний, другой);
#         - дата размещения (день недели, месяц, год).
# - [ ]  Выполнено задание «Посчитайте среднюю цену одного квадратного метра в 10 населённых пунктах с наибольшим числом объявлений»:
#     - выделены населённые пункты с самой высокой и низкой стоимостью квадратного метра.
# - [ ]  Выполнено задание «Выделите квартиры в Санкт-Петербурге с помощью столбца `locality_name` и вычислите их среднюю стоимость на разном удалении от центра»:
#     -  учтён каждый километр расстояния, известны средние цены квартир в одном километре от центра, в двух и так далее;
#     -  описано, как стоимость объекта зависит от расстояния до центра города;
#     -  построен график изменения средней цены для каждого километра от центра Петербурга.
# - [ ]  На каждом этапе сделаны промежуточные выводы.
# - [ ]  В конце проекта сделан общий вывод.

# In[ ]:





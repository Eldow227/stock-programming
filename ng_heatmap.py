# -*- coding: utf-8 -*-


import yfinance as yf
import pandas as pd
import math
import numpy as np
import seaborn as sb
import missingno as msno



ng = yf.download("NG=F", start="2000-01-01", end="2021-12-31")
del ng["Adj Close"]
ng["Year"] = ng.index.year
ng["day_of_week"] = ng.index.weekday
ng["day_of_year"] = ng.index.dayofyear
ng["day_of_month"] = ng.index.day
ng["month"] = ng.index.month
#---------------------------------------
ng["log"] = log(ng["Close"])
ng["log_diff"] = (ng["log"]).diff()
ng["volatility"] = pow(ng["log_diff"], 2)
ng["amplituda"] = ng["High"]/ng["Low"]
ng["opcl"] = ng["Open"] - ng["Close"]

# %%
ng.to_excel("ng_1.xlsx", sheet_name = "ng_data", index = True)
# %%
def Tracker(values, columns):
    len_v = len(values)
    len_col = len(columns)
    index=0
    return ng[(ng[columns[index]] == values[index]) & (ng[columns[index+1]] == values[index+1])]
    
    

x = Tracker([8, 6], ["month", "day_of_month"])

print(x)


# 1 - day_of_month
# 8 - month
# %%
print(ng.loc[(ng["month"].isin([8])) & (ng['day_of_month'] == )])
# %%
print(ng.iloc[2])
# %%
def Tracker(values, columns):
    counter = 0
    lenght = len(ng)
    index = 0
    result = []
    if len(values) > 1 and len(columns) > 1:
        while index != len(ng)-1:
            if values[counter] == getattr(ng.iloc[index], columns[counter]) and values[counter+1] == getattr(ng.iloc[index], columns[counter+1]):
                result.append(index)
                index += 1
            else:
                index += 1
        
    else:
        while index != len(ng)-1:
            if values[counter] == getattr(ng.iloc[index], columns[counter]):
                result.append(index)
                index += 1
            else:
                index += 1
    return ng.iloc[result]

print(Tracker([1, 2], ["month", "day_of_month"])["log_diff"])

# %%
def Tracker(value, column):
    return ng.loc[ng[column]==value]

x = Tracker(2020, "Year")

x.to_excel("x1.xlsx", sheet_name = "x1", index = True)

# %%
print(Tracker(6, "month"))
# %%
def conditions(conds, ng):
    to_return = ng.where(conds[0])
    to_return.dropna(inplace=True, how="any")
    return to_return
    
print(conditions())

# %% #SREDNIA


i = [num for num in range(0,30)]
x= [num for num in range(0,365)]
result = []
for num in i:
    for num1 in x:
        result.append(num*num1)
# %%
print(pd.DataFrame({"numbers": i, "numbers2":x}, index=range(31), columns=range(365)))
# %%

x= sb.heatmap(ng["month"])
# %%
data = sb.load_dataset(ng)
data = data.pivot(["day_of_month"], "month", sum("log_diff")/len("year"))
show = sb.heatmap(data)
# %%
# %%

df = pd.DataFrame({'month': [2, 5, 8, 10],
                   'year': [2017, 2019, 2018, 2019],
                   'sale': [60, 45, 90, 36]})

df.set_index([pd.Index([2,3,4,5]),'month'])
print(df)







# %%
Index = range(1, 32)
Cols = range(1, 13)

df = pd.DataFrame(columns = Cols, index = Index)

for month in range(1, 13):
    for day in range( 1, 31):
        
        df.xs(day)[month] = (Tracker([month, day], ["month", "day_of_month"])["log_diff"].sum())/21
        

# %%
df.dropna(inplace=True, how='any')


print(df)
# %%
print(df.iloc[0, 0])
# %%
x = sb.heatmap(df, cmap="YlGnBu", mask=df.isnull(),annot=True, fmt='d')


# %%
import missingno

# %%

def conditions(conds, all_data=ng, wykres=False):
    to_return = all_data.where(conds[0])
    to_return.dropna(inplace=True, how='any')
    
    if wykres:
        plt.plot(to_return.log_diff)
        plt.axhline(0, c="black")
        plt.show()
        
    return to_return

print(conditions(["month" == 1]))

# %%

log_diff = []

log_diff.append(Tracker([1, 5], ["month", "day_of_month"])["log_diff"])

x = sum(log_diff)/len(log_diff)

print(x)
# %%

for i in rneg()

# %%
print(Tracker([9, 1], ["month", "day_of_month"])["log_diff"])





# %%
print(ng["log_diff"].mean())





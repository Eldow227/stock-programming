# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 10:58:52 2021

@author: kmate
"""

# %%
##TWORZYMY WYKRES O CENACH AKCJI (30-D)
import random
import matplotlib.pyplot as plt
import find_tops
values= []
days = [i for i in range(1, 31)]
while len(values) < 30:
    values.append(random.randint(20, 70))

# print(len(values))
# print(len(days))
fig, ax = plt.subplots()
plt.plot([day for day in days], [value for value in values])
plt.axis([0, 30, 0, 100])
plt.show()
line = ax.lines[0]
ax.set_title('TEST PLOT')
COORDINATES = line.get_xydata()
print('Done!')
# %%
second = {}
x_to_y_dict = {}
for i in COORDINATES:
    x_to_y_dict[i[0]] = i[1]
for i in COORDINATES:
    second[i[0]] = i[1]

print(x_to_y_dict)
# %%
##ZNAJDUJE X DLA DANEGO Y

def show_x(y_value):
     """Give y value to see its x."""
     for key, value in x_to_y_dict.items():
         if y_value == value:
             del x_to_y_dict[key]
             return key
         
tops_coordinates = []
x_list = []
y_list = []
for y in find_tops.tops(values):
    y_list.append(y)
    x_list.append(show_x(y))
print(x_list)

tops_coordinates.append(y_list)
tops_coordinates.append(x_list)
print('Done!')
print(tops_coordinates)
# %%
print('*'*10)
print(y_list)
print(x_list)
print('*'*10)
print('Checking if correct...')
anomaly = []
indexes = []
for i in range(1, len(x_list)):
    if x_list[i] < x_list[i-1]:
        anomaly.append(x_list[i])
        indexes.append(i)
        
for i in anomaly:
    if i in x_list:
        x_list.remove(i)
        
for i in indexes:
    y_list.remove(y_list[i])
print('*'*10)
print(y_list)
print(x_list)
# %%
# print(x_to_y_dict)
# cure = []
# for i in anomaly:
#     cure.append(second[i])
#     del second[i]
    
# print(cure)

# for c in cure:
#     x_list.append(show_x(c))
# # %%
# print(x_to_y_dict.items())
    
    
    



# %%
##RYSUJ NOWY WYKRES Z ZAZNACZONYMI SZCZYTAMI
print(tops_coordinates)
fig, ax = plt.subplots()
plt.plot([day for day in days], [value for value in values], tops_coordinates[1], tops_coordinates[0])
plt.axis([0, 30, 0, 100])
plt.show()
line = ax.lines[0]
ax.set_title('TEST PLOT')
COORDINATES = line.get_xydata()
print('Done!')
# %%
print(COORDINATES)

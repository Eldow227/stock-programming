# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 13:29:08 2021

@author: kmate
"""
# case1 = [2, 4, 3, 5, 3, 4, 1, 0, 7, 5, 8, 2, 3, 1] # 4, 5, 4, 7, 8, 3
case2 = [4, 2, 3, 1, 5, 2, 8, 1, 2, 3, 5] # 4, 3, 5, 8
def tops(list_of_values):
    """The idea of this function is to find every top in the collection of numbers."""
    index = 0
    result = []
    while index <= len(list_of_values):
        
        print(f'Working...')
        print(f'Current index: {index}')
        if index == 0:
            if list_of_values[index] > list_of_values[index+1]:
                result.append(list_of_values[index])
                print(f'Added! index: {index}')
                index += 1
            elif  list_of_values[index] < list_of_values[index+1]:
                print(f'Passed! index: {index}')
                index += 1
            
            
        elif index > 0 and index+1 < len(list_of_values):
            if list_of_values[index-1] < list_of_values[index] > list_of_values[index+1]:
                result.append(list_of_values[index])
                print(f'Added! index: {index}')
                index += 1
            else:
                print(f'Passed! index: {index}')
                index += 1
            
                
        elif index+1 == len(list_of_values):
            print(list_of_values[index])

            if list_of_values[index] > list_of_values[index-1]:
                print(f'Added! index: {list_of_values[index]}')
                result.append(list_of_values[index])
                break
            else:
                break

                
                
            
        
    print('Done!')
    return result

print(tops(case2))
# %%
# index: 0, 1, 2, 3, 4, 5, 6, 7, 8
# dlugosc: 1, 2, 3, 4, 5, 6, 7, 8
print(len(case2))

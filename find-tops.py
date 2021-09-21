# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 13:29:08 2021

@author: kmate
"""
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



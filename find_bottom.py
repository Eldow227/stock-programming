# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 19:05:46 2021

@author: kmate
"""
###----!IN NEED OF REPAIR!---###
def bottom(list_of_values):
    """The goal of this function is to find every bottom number in set."""
    index = 0
    result = []
    print('Starting looking for bottoms.')
    while index <= len(list_of_values):
        
        print('Working...')
        if index == 0:
            if list_of_values[index] < list_of_values[index+1]:
                result.append(list_of_values[index])
                print(f'Added! index: {index}')
                index += 1
                
            elif  list_of_values[index] > list_of_values[index+1]:
                print(f'Passed! index: {index}')
                index += 1
                
        elif index > 0 and index+1 < len(list_of_values):
            if list_of_values[index-1] > list_of_values[index] < list_of_values[index+1]:
                result.append(list_of_values[index])
                print(f'Added! index: {index}')
                index += 1
            else:
                print(f'Passed! index: {index}')
                index += 1
        elif index+1 == len(list_of_values):
            if list_of_values[index-1] > list_of_values[index]:
                result.append(list_of_values[index])
                print(f'Added! index: {index}')
                break
            else:
                print(f'Passed! index: {index}')
                break
        
        
    print('Done!')       
    return result


print(bottom([5, 1, 5, 2]))

            


                
                
            
            
        
    
    
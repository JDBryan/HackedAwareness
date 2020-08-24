# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:27:30 2020

@author: alexa
"""

def accounts_2_dict(service_name):
    
    file = open(service_name)
    
    password_link = file.readline()
    
    temp_line = file.readline()
    
    accounts = {}
    
    while temp_line:
        accounts[temp_line.split()[0]] = temp_line.split()[1]
        temp_line = file.readline()
        
    file.close()
    
    return accounts, password_link

print(accounts_2_dict("Google.txt"))
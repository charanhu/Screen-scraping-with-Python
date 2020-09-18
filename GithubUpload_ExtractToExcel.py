# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 10:45:16 2020

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 11:15:37 2020

@author: Vijay Jayachandran
"""

import requests
import xlsxwriter
from bs4 import BeautifulSoup

for i in range(3):
    if i > 0:
        URL = 'https://www.yellowpages.ca/search/si/'+str(i)+'/consulting+engineer/Victoria+BC'
        page = requests.get(URL)
        
        soup = BeautifulSoup(page.content, 'html.parser')
        
        results = soup.find_all("div", class_="listing_right_section")
        
        workbook = xlsxwriter.Workbook('LocalPathToExtract'+str(i)+'.xlsx') 
        worksheet = workbook.add_worksheet("Extract") 
        print(URL,i)
        counter = 0
        row1 = 0
        for row in results:          # Print all occurrences
            stuff = row.get_text()
            mylist = stuff.split('\n')
            new_str = ""
            col = 0
            for item in mylist:
                if item:
                    worksheet.write(row1, col, item) 
                    new_str += item + '\n'
                    col += 1
            #print(new_str)
            counter+= 1
            #print(counter)
            row1 += 1
    
    workbook.close() 

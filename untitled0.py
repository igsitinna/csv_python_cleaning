# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 10:47:41 2022

@author: Печарська
"""

import pandas as pd
#access to original file:
df = pd.read_csv("H:\Нова папка\data-export (3).csv", index_col=0)
print(df)
print("________________________________________________________________________________________________")

#extract required rows, assign required datatype:
df_part_1 = df.iloc[0:28].astype("float64")


#sum up the values in columns:
summed_columns_df_part_1 = df_part_1.sum(axis=0, skipna = True)
 
all_summed = summed_columns_df_part_1.sum(axis=0, skipna = True)


#calculate percentage:
pers_col = []
for row in summed_columns_df_part_1:
    persentage = (row / all_summed) * 100
    pers_col.append(persentage.round(1))

    
#add list with persentage as a column to the DataFrame
final_df_part_1 = pd.DataFrame(summed_columns_df_part_1)
final_df_part_1['persentage'] = pers_col
final_df_part_1.columns = ['event_count', 'percentage, %']
print(final_df_part_1)

 
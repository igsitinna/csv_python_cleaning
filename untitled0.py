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
"""OUTPUT:
    runfile('D:/untitled0.py', wdir='D:')
                                                          page_view  ... session_start
    Day                                                              ...              
    0000                                                          0  ...           0.0
    0001                                                          0  ...           0.0
    0002                                                          0  ...           0.0
    0003                                                          0  ...           0.0
    0004                                                          0  ...           0.0
    0005                                                          0  ...           0.0
    0006                                                          0  ...           0.0
    0007                                                          0  ...           0.0
    0008                                                          8  ...           5.0
    0009                                                          0  ...           0.0
    0010                                                          0  ...           0.0
    0011                                                         12  ...           6.0
    0012                                                          1  ...           1.0
    0013                                                          9  ...           1.0
    0014                                                          0  ...           0.0
    0015                                                          0  ...           0.0
    0016                                                          0  ...           0.0
    0017                                                          0  ...           0.0
    0018                                                          0  ...           0.0
    0019                                                          0  ...           0.0
    0020                                                          0  ...           0.0
    0021                                                          0  ...           0.0
    0022                                                          0  ...           0.0
    0023                                                          0  ...           0.0
    0024                                                          0  ...           0.0
    0025                                                          0  ...           0.0
    0026                                                          5  ...           2.0
    0027                                                         11  ...           5.0
    # Report CSV Export                                         NaN  ...           NaN
    # Account: igsit                                            NaN  ...           NaN
    # Property: https://sites.google.com/view/igsit...          NaN  ...           NaN
    # Start date: 20220602                                      NaN  ...           NaN
    # End date: 20220629                                        NaN  ...           NaN
    # Start date: 20220602                                      NaN  ...           NaN
    # End date: 20220629                                        NaN  ...           NaN
    Event name                                          Event count  ...           NaN
    page_view                                                    46  ...           NaN
    click                                                        39  ...           NaN
    user_engagement                                              28  ...           NaN
    scroll                                                       21  ...           NaN
    session_start                                                20  ...           NaN
    first_visit                                                   5  ...           NaN
    # All Users                                                 NaN  ...           NaN
    # Start date: 20220602                                      NaN  ...           NaN
    # End date: 20220629                                        NaN  ...           NaN
    Event name                                          Event count  ...           NaN
    page_view                                                    46  ...           NaN
    click                                                        39  ...           NaN
    user_engagement                                              28  ...           NaN
    scroll                                                       21  ...           NaN
    session_start                                                20  ...           NaN
    first_visit                                                   5  ...           NaN

    [52 rows x 5 columns]
    ________________________________________________________________________________________________
                     event_count  percentage, %
    page_view               46.0           29.9
    click                   39.0           25.3
    user_engagement         28.0           18.2
    scroll                  21.0           13.6
    session_start           20.0           13.0
    """

 
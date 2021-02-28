import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
sb.set() # set the default Seaborn style for graphics

pd.set_option('display.max_column',None)
pd.set_option('display.max_rows',None)

#pre2k=pd.read_csv('approval-date-1990-1999.csv')
post2k=pd.read_csv('approval-date-2000-feb-2012.csv')

sb.set(rc={'figure.figsize':(11.7,8.27)})
sb.barplot(x='resale_price', y='town', data=post2k)
plt.show()

'''sb.barplot(x='resale_price', y='flat_type', data=post2k, order=["1 ROOM", "2 ROOM", "3 ROOM", "4 ROOM", "5 ROOM", "EXECUTIVE", "MULTI-GENERATION"])

sb.pointplot(x='month', y='resale_price', data=post2k)

post2k['year']=post2k['month'].str[:4]
sb.pointplot(x='year', y='resale_price', data=post2k)

sb.barplot(x='year', y='resale_price', data=post2k)'''



import pandas as pd
from i__init__ import p1

def file_read(a1='SIE_b'):  
  file=p1+a1+'.csv' 
  df=pd.read_csv(file)
  print('-----READ---',a1,'-------:', file)
  return df
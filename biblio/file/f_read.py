import pandas as pd
from pathlib import Path
import os
path =  os.path.join(Path(os.path.abspath(os.path.dirname(__file__))+'\\').parent.parent, "inout\\")
path2 =  os.path.join(Path(os.path.abspath(os.path.dirname(__file__))+'\\').parent, "const\\")

def file_read(a1='SIE_b'):
  file=path+a1+'.csv'
  df=pd.read_csv(file)
  print('-----READ---',a1,'-------:', file)
  return df

def file_read2(a1='SIE_b'):
  file=path2+a1+'.csv'
  df=pd.read_csv(file)
  print('-----READ---',a1,'-------:', file)
  return df
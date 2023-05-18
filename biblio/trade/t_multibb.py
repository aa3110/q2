import numpy as np
from t_sma import sma
from c_constant import nb
from t_rstd import rstd

def bb(df=None,a1='Close',val1=None):
  b1='bbm'+str(val1);b2='bbh'+str(val1);b3='bbl'+str(val1);s1='std'+str(val1)
  df[b1]=sma(df,a1,val1)
  df[b2]=df[b1]+(nb*rstd(df,a1,val1))
  df[b3]=df[b1]-(nb*rstd(df,a1,val1))
  df.drop([s1], axis=1, inplace=True)
  return df[b1],df[b2],df[b3]

def multibb(df=None,a1='Close',*va):
  k1=[]
  def k_name(i2='',value=''):j=(bb(df,a1,value)[i2]).name;k1.append(j)
  [k_name(i2,value) for value in va for i2 in range(3)] 
  return k1
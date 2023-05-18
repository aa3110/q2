from t_sma import sma
from t_rstd import rstd

def cci(df=None,a1='Close',val1=None):
  ar,df[ar]='CCI'+str(val1),None;s1='std'+str(val1)
  df[ar]=(df[a1]-sma(df,a1,val1))/(0.01*rstd(df,a1,val1))
  df.drop([s1], axis=1, inplace=True) 
  return df[ar]

def multicci(df=None,a1='Close',*va):
  k1=[]
  for value in va: j=cci(df,a1,value).name; k1.append(j)
  k1.append('g100');k1.append('g-100')   
  df['g100']=100;df['g-100']=-100;k1.append('g100');k1.append('g-100')
  return k1 
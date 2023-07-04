import numpy as np

def high(df=None,a1='Close',a2='bbh'):
  a2=str(a2);(ar1,df[ar1])=(a1+'>'+a2,None) 
  df[ar1]=np.where(df[a1]>=df[a2],df[a1],None)
  return df[ar1][df.shape[0]-1]

def low(df=None,a1='Close',a2='bbh'): 
  a2=str(a2);(ar2,df[ar2])=(a1+'<'+a2,None)   
  df[ar2]=np.where(df[a1]<=df[a2],df[a1],None)
  return df[ar2][df.shape[0]-1]

def highlow(df=None,a1='Close',a2='bbh'):  
  a2=str(a2); (ar1,ar2)=(a1+'>'+a2,a1+'<'+a2);(df[ar1],df[ar2])=(None,None)
  df[ar1]=np.where(df[a1]>=df[a2],df[a1],None)   
  df[ar2]=np.where(df[a1]<=df[a2],df[a1],None)
  return df[ar1][df.shape[0]-1], df[ar2][df.shape[0]-1]
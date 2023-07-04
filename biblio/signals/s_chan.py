import numpy as np

def chan_in(df=None,a1='Close',a2='bbl',a3='bbh'): 
  (a1,a2,a3)=(str(a1),str(a2),str(a3))
  (ar1,df[ar1])=(a1+'in'+a2+a3,None)
  df[ar1]=np.where((df[a1]>=df[a2])&(df[a1]<=df[a3]),df[a1],None) 
  return df[ar1][df.shape[0]-1]

def chan_out(df=None,a1='Close',a2='bbl',a3='bbh'): 
  (a1,a2,a3)=(str(a1),str(a2),str(a3))
  (ar1,df[ar1])=(a1+'out'+a2+a3,None)
  df[ar1]=np.where((df[a1]<df[a2])or(df[a1]>df[a3]),df[a1],None) 
  return df[ar1][df.shape[0]-1]

def chan_ot(df=None,a1='Close',a2='bbl',a3='bbh'): 
  (a1,a2,a3)=(str(a1),str(a2),str(a3))
  (ar1,df[ar1])=(a1+'ot'+a2+a3,None)
  df[ar1]=np.where((df[a1]>=df[a3])&(df[a1].shift(-1)<=df[a3].shift(-1)),df[a1],None) 
  return df[ar1][df.shape[0]-1]

def chan_it(df=None,a1='Close',a2='bbl',a3='bbh'): 
  (a1,a2,a3)=(str(a1),str(a2),str(a3))
  (ar1,df[ar1])=(a1+'it'+a2+a3,None)
  df[ar1]=np.where((df[a1]<=df[a3])&(df[a1].shift(-1)>=df[a3].shift(-1)),df[a1],None) 
  return df[ar1][df.shape[0]-1]

def chan_ib(df=None,a1='Close',a2='bbl',a3='bbh'): 
  (a1,a2,a3)=(str(a1),str(a2),str(a3))
  (ar1,df[ar1])=(a1+'ib'+a2+a3,None)
  df[ar1]=np.where((df[a1]>=df[a2])&(df[a1].shift(-1)<=df[a2].shift(-1)),df[a1],None) 
  return df[ar1][df.shape[0]-1]

def chan_ob(df=None,a1='Close',a2='bbl',a3='bbh'): 
  (a1,a2,a3)=(str(a1),str(a2),str(a3))
  (ar1,df[ar1])=(a1+'ob'+a2+a3,None)
  df[ar1]=np.where((df[a1]<=df[a2])&(df[a1].shift(-1)>=df[a2].shift(-1)),df[a1],None) 
  return df[ar1][df.shape[0]-1]
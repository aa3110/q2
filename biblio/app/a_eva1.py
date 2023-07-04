from t__init__ import multibbh,multibbl,multibbm,multisma
from a__init__ import alpha_there

def eva1(df='',da='',w2='',i=0):
  p0=da[w2][i];p0=str(p0)
  if alpha_there(p0)==False: df[p0]=da[w2][i]=eval(p0) 
  else: da[w2][i]=eval(p0)[0]   
        
def rmax(df=None,a1='Close',val1=None):
  (ar,df[ar])=('rmax'+str(val1),None)
  df[ar]=df[a1].rolling(val1).max()
  return df[ar]

def rmin(df=None,a1='Close',val1=None):
  (ar,df[ar])=('rmin'+str(val1),None)
  df[ar]=df[a1].rolling(val1).min()
  return df[ar]

def multirmx(df=None,a1='Close',*va):
  k1=[]
  for value in va: j1=rmax(df,a1,value).name; j2=rmin(df,a1,value).name; k1.append(j1); k1.append(j2)  
  return k1
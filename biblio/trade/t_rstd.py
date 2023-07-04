def rstd(df=None,a1='Close',val1=None): 
  (ar,df[ar])=('std'+str(val1),None)
  df[ar]=df[a1].rolling(val1).std()
  return df[ar]
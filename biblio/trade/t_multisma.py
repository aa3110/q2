def sma(df=None,a1='Close',val1=None):
  ar,df[ar]=a1+str(val1),None
  df[ar]=df[a1].rolling(val1).mean()
  return df[ar]

def multisma(df=None,a1='Close',*va):
  k1=[]  
  for value in va: j=(sma(df,a1,value)).name; k1.append(j)
  return k1
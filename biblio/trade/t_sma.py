def sma(df=None,a1='Close',val1=None):
  ar,df[ar]=a1+str(val1),None
  df[ar]=df[a1].rolling(val1).mean()
  return df[ar]
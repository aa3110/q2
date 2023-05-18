def aroonhigh(df=None,a1='Close',val1=None): 
  ar,df[ar]='Closeah'+str(val1),None; e1=val1+1
  for i in range(df[a1].shape[0]-1,e1,-1):
    lis=df[a1][i-val1:i+1]
    m1=max(lis)
    for counter, value in enumerate(lis):
      if (value==m1) :pos=counter
    df[ar][i]=100*pos/val1    
  return df[ar]

def aroonlow(df=None,a1='Close',val1=None):
  ar,df[ar]='Closeal'+str(val1),None; e1=val1+1
  for i in range(df[a1].shape[0]-1,e1,-1):
    lis=df[a1][i-val1:i+1]
    m1=min(lis)
    for counter, value in enumerate(lis):
      if (value==m1) :pos=counter
    df[ar][i]=100*pos/val1   
  return df[ar]

def multiaroon(df=None,a1='Close',*va):
  k1=[]
  for value in va:    
    n1=(aroonhigh(df,'Close',value)).name; n2=(aroonlow(df,'Close',value)).name; k1.append(n1); k1.append(n2)   
  return k1

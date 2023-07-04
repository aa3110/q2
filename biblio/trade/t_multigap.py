def gap(df=None,a1='Close',val1=None):
  a2='Open'; a3=a1+a2
  df[a3]=(df[a1]-df[a2])  
  return df[a3]

def multigap(df=None,a1='Close',*va):
  k1=[]
  for value in va: 
    j=gap(df,a1,value).name; k1.append(j)
    df['g0']=0;k1.append('g0')
  return k1
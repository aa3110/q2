def gap(df=None,a1='Close',val1=None):
  a2='Open'; a3=a1+a2
  df[a3]=(df[a1]-df[a2])  
  return df[a3]

def multigap(df=None,a1='Close',*va):
  k1=[]
  def k1_name(value=''):j=gap(df,a1,value).name; k1.append(j)
  [k1_name(value) for value in va]  
  df['g0']=0;k1.append('g0') 
  return k1
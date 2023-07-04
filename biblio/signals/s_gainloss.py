import numpy as np

def gain(df=None,a1='Close',a2=200,p1=10): 
  e1=df.shape[0]-1;last1=df[a1][e1];cur3=None
  cur1=(df[a1][e1]/a2)-1;cur2=round(cur1*100,2)
  if (p1>0) & (last1>a2) & (cur2>p1): cur3=cur2    
  return cur3

def loss(df=None,a1='Close',a2=200,p1=10): 
  e1=df.shape[0]-1;last1=df[a1][e1];cur3=None
  cur1=(df[a1][e1]/a2)-1;cur2=round(cur1*100,2)  
  if (p1<0) and (last1<a2) and (cur2<p1): cur3=cur2  
  return cur3

def gainloss(df=None,a1='Close',a2=200,p1=10): 
  e1=df.shape[0]-1;last1=df[a1][e1];cur3=None
  cur1=(df[a1][e1]/a2)-1;cur2=round(cur1*100,2)
  if (p1>0) & (last1>a2) & (cur2>p1): cur3=cur2
  if (p1<0) and (last1<a2) and (cur2<p1): cur3=cur2  
  return cur3
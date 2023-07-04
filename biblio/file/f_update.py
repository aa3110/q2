import pandas as pd
import numpy as np
import yfinance as yf
from datetime import date
from pathlib import Path
import os

from i__init__ import p1

def file_update(stock='SIE',start='2020-01-01'):  
  file = p1+stock+'.csv' 
  
  def dl(stock=stock,start=start,end=str(date.today())):
    power=yf.Ticker(stock+'.DE')     
    df=power.history(start=start, end=str(date.today()))   
    df=df.drop('Dividends', axis=1).drop('Stock Splits', axis=1)
    return df

  def new(start=start):
    df=dl()
    df.to_csv(file, index=True, header=True, decimal='.', sep=',', float_format='%.6f')
    print('-----NEW:',file)
    return df
  
  def update(file=''):
    df=pd.read_csv(file) 
    d_start=df['Date'][(df.shape[0]-1)]
        
    da=dl(stock=stock,start=d_start,end=str(date.today()))
    da=da.reset_index(drop=False)
    da['Date'] = da['Date'].dt.strftime('%Y-%m-%d')
    
    frames=[df,da]
    db = pd.concat(frames).drop_duplicates(subset=['Date'])  
    db.to_csv(file, index=False, header=True, decimal='.', sep=',', float_format='%.2f')
    print('-----UPDATED done:',file)
    return df

  if Path(file).is_file(): df=update(file)    
  else: df=new()
  
  return df
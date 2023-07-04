import numpy as np

def layout(da=[]):
  cash=10000
  broker=40 #USD
  tax=50 #%
  da['buy']=(da['qty']*da['value'])
  da['qty_sum']=da['qty'].cumsum()
  da['invest']=da['buy'].cumsum()
  da['market_value']=da['qty_sum']*da['value']
  da['rendite']=da['market_value']-da['invest']
  da['rendite%']=da['rendite']/da['invest']*100
  da['broker']=broker
  da['tax']=(da['rendite']-da['broker'])*tax/100
  da['tax']=np.where(da['tax']>0,da['tax'],0)
  da['profit']=da['rendite']-da['broker']-da['tax']
  da['cash']=cash-da['invest']
  da['depot']=da['market_value']+da['cash']
  da['broker_sum']=da['broker'].cumsum()
  da['tax_sum']=da['tax'].cumsum()
  da['cost_sum']=da['broker_sum']+da['tax_sum']
  return da
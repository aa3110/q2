import path_def.pat1
from f__init__ import file_read,file_save,fsort
from b_lay import layout

def bus_cr(dep='depot1'):  
  da=fsort(dep,'stock');da['value']=None
  
  li2=list(set(da['stock']));li2.sort()
  
  for j in range(len(li2)): 
    a1=li2[j];df=file_read(a1)
    
    for i in range(da.shape[0]-1):    
      d1=da['Date'][i]
      da['value'][(da['Date']==d1) & (da['stock']==a1)]=(float(df['Close'][df['Date']==d1])) 
  layout(da)
  
  for i in list(da)[3:]:da[i]=da[i].values.astype(float).round(decimals =2)  
  
  file_save('depot_out1',da) 
    
  return 

bus_cr('depot1')
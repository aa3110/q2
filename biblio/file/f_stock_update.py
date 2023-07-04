from f__init__ import file_read,file_update
from i__init__ import p1

def stock_update(a1='alert'):  
  da=file_read(a1)  
  li1=list(set(da['stock']))
  
  [file_update(li1[i],'2022-01-01') for i in range(len(li1))]
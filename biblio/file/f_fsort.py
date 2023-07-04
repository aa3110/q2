from f__init__ import file_read,file_save

def fsort(dep='depot1',sor='stock'):
  dep1=dep+'_inp'  
  da=file_read(dep1).sort_values(by=[sor]).reset_index(drop=True)
  file_save(dep1,da)
  return da
from i__init__ import p1

def file_save(a1='SIE_b',df=None):
  file=p1+a1+'.csv'
  df.to_csv(file, index=False, header=True, decimal='.', sep=',', float_format='%.2f')
  print('-----SAVED---:',file)
  return #file
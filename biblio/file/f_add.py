import pandas as pd
from pathlib import Path
import os
path =  os.path.join(Path(os.path.abspath(os.path.dirname(__file__))+'\\').parent, "const\\")

def file_add(st1=''):  
  s2='sto1='+str(st1)
  file=path+"c_constant.py"
  f1 = open(file, "a"); f1.writelines('\n'); f1.writelines(s2); f1.close() 
  print('-----ADD---',s2,'-------:',file)
  return
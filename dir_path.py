import os,sys
from pathlib import Path

pr_name=Path(__file__).parent.resolve().name

mis=('.','__pycache__')

def prj(pr_name=''):
  pr_dir = [p for p in  Path(__file__).parents if p.parts[-1]==pr_name][0] 
  return pr_dir

def fast_scandir(dn):
    subdir= [f.path for f in os.scandir(dn) if f.is_dir()]
    for st in mis: subdir = [i for i in subdir if st not in i]    
    [subdir.extend(fast_scandir(dn)) for dn in list(subdir)]
    return subdir
  
for i1 in fast_scandir(prj(pr_name)):  
  if (os.path.join(i1) not in  sys.path) : sys.path.insert(0, os.path.join(i1))

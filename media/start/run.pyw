import path_def.pat1
from f__init__ import file_read
from m__init__ import msgbox,mail_sent
from playsound import playsound
from pathlib import Path
import os
path =  os.path.join(Path(os.path.abspath(os.path.dirname(__file__))+'\\').parent, "inout\\")

f1='sig';p1=path+'not1.wma'; n1='signal'
mes1=file_read(f1).to_string()

msgbox(mes1,n1)
mail_sent(n1,mes1)
playsound(p1)
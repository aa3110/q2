from bib__init__ import file_read,msgbox,mail_sent
from playsound import playsound
from i__init__ import p1

f1='sig';s1=p1+'not1.wma'; n1='signal'
mes1=file_read(f1).to_string()

msgbox(mes1,n1)
mail_sent(n1,mes1)
playsound(s1)
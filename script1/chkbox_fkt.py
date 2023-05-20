from tkinter import Tk,Checkbutton,Button,Spinbox,IntVar,Scale,HORIZONTAL
from functools import partial
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt
import numpy as np
from itertools import cycle
from p__init__ import pltimpix
from t__init__ import fkt1,fkt2
from a__init__ import dfclose,new_var
from c__init__ import col1,plr,hor1
col2_cy=cycle(col1);no1_cy=cycle(list(range(10)))
fkt=fkt1+fkt2

def r1(self):
  ee=len(fkt);e1=len(fkt1)
  var=new_var(hor1)
  self.df=dfclose(self.df,self.sto2)

  def set_all():
    [var[0][i].set(0) for i in range(ee+2)]
    [[var[j][i].set(self.sval[0]) for j in range(1,hor1)] for i in range(ee+2)]
    return var

  def func():
    t=new_var(ee+2)     

    def t_add(i2='',j2=''): t[i2]+=fkt[i2](self.df,'Close',var[j2][i2].get());t[i2]=list(set(t[i2]))  
    def t_sto2(i3=''): t[i3]=self.sto2
    [[t_add(i2,j2) for j2 in range(1,hor1) if var[0][i2].get() == 1] for i2 in range(ee)]    
    [t_sto2(i3) for i3 in (ee,ee+1) if var[0][i3].get() == 1]  
   
    ax=new_var(10)
    fig=plt.figure(figsize=(12,10),dpi=300); ax[0]=fig.add_subplot(111)
    for i in range(1,10): ax[i]=ax[0].twinx()

    (p0,p1)=(w0.get(),w1.get())
    x1=self.df['Date'][p0:p1].index.values
    if ((var[0][ee].get() == 0) and (var[0][ee+1].get() == 0)):
      ax[0].plot(x1, self.df['Close'][p0:p1],color='blue')
    [ax[0].plot(x1, self.df[y0][p0:p1]) for i2 in range(e1) for y0 in t[i2]]
    [[ax[i].plot(x1, self.df[y0][p0:p1],color=next(col2_cy)) for i in range(e1,ee) for y0 in t[i]]]        
    for i,y0 in enumerate(t[ee]): ax[0].plot(x1, self.df[y0][p0:p1],color=col1[i]) 
    for i,y0 in enumerate(t[ee+1]): ax[next(no1_cy)].plot(x1, self.df[y0][p0:p1],color=col1[i],linestyle='dashed')
      
    self.lab0.setPixmap(QPixmap(pltimpix(plt)))

  app = Tk()
  [var[j].append(IntVar()) for j in range(hor1) for i in range(ee+2)] 

  w0 = Scale(app, from_=0, to=plr[1], orient=HORIZONTAL);w0.grid(row=ee+1, column=0);w0.set(self.plr[0])
  w1 = Scale(app, from_=0, to=plr[1], orient=HORIZONTAL);w1.grid(row=ee+1, column=1);w1.set(self.plr[1])

  for i in range(ee):
    Checkbutton(app, text=fkt[i].__name__, variable=var[0][i], command=partial(func)).grid(row=i, column=0)
    [Spinbox(app, values=self.sval,width=5,textvariable=var[j][i],wrap=True).grid(row=i,column=j,padx=2,pady=2)  for j in range(1,hor1)]   
  [Checkbutton(app, text='cha'+str(h1), variable=var[0][i+1+h1], command=partial(func)).grid(row=i+1, column=h1) for h1 in (0,1)]

  Button(app, text='Quit', command=app.destroy,bg="red").grid(row=ee+1, column=hor1+1)
  Button(app, text='reset', command = set_all,bg="cyan").grid(row=ee+2, column=hor1+1)  
  Button(app, text='update', command = partial(func),bg="yellow").grid(row=ee+2, column=hor1)
  app.mainloop() 
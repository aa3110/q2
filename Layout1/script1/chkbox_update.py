from tkinter import Tk,Button,Label,Entry,StringVar
from functools import partial
from f__init__ import file_update,f_add

def r2(self):  
  def update1(value): [file_update(s1,self.start) for s1 in self.sto1] 
  def s1(): self.sto1.append(v1.get());f_add(self.sto1)

  app = Tk()     
  v1=StringVar()
   
  Label(app, text="stock-ID:").grid(row=0, column=0) 
  Entry(app, textvariable=v1).grid(row=1, column=0)     
 
  Button(app, text='ADD', command=s1,bg='cyan').grid(row=1, column=1,padx=10,pady=10)  
  Button(app, text='update', command = partial(update1, False),bg='yellow').grid(row=2, column=0,padx=10,pady=10)  
  Button(app, text='Quit', command=app.destroy,bg='red').grid(row=2, column=1,padx=10,pady=10)
    
  app.mainloop()
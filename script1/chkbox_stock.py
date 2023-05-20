from tkinter import Tk, Checkbutton, IntVar,Button
from functools import partial
from f__init__ import file_read

def r0(self):  
  def func(i):
    if var1[i].get() == 1: self.df=file_read(self.sto1[i]); self.sto2.append(self.sto1[i])          
  def set_all(value): [v.set(value) for v in var1]
   
  app = Tk()  
  
  var1 = []; [var1.append(IntVar()) for i in range(len(self.sto1))]    
 
  for i,fu in enumerate(self.sto1):
   Checkbutton(app, text=f'{fu} {i}', variable=var1[i], pady=0, command=partial(func, i)).grid(row=i%3, column=i//3)      
  
  Button(app, text='Quit', command=app.destroy,bg="red").grid(row=2, column=i+1)
  Button(app, text='reset', command = partial(set_all, False),bg="cyan").grid(row=3, column=i+1)   
  app.mainloop()
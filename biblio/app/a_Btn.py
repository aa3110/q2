from PyQt5.QtWidgets import QToolButton

def Btn(self,tab,con,i,txt,x1,y1):    
  a1='self.btn' + str(i)
   
  v1 = {}  
  v1[a1] = QToolButton(tab)  
  v1[a1].setText(str(txt))
  v1[a1].move(x1,y1)
  v1[a1].clicked.connect(con)   
  return v1[a1]
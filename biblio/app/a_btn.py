from PyQt5.QtWidgets import QToolButton

def btn(self,tab,con,i):    
  a1='self.btn' + str(i)
   
  v1 = {}  
  v1[a1] = QToolButton(tab)
  v1[a1].move((i+1)*100-100,20)
  v1[a1].setText("chkbox_"+str(i))
  v1[a1].clicked.connect(con)   
  return v1[a1]
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap

def QLab(self,tab,p1,w,h,i,x1,y1):
  a1='self.lab' + str(i)
  
  v1 = {}
  v1[a1] = QLabel(tab)  
  v1[a1].setGeometry(0, 50, w, h)
  v1[a1].move(x1,y1)
  v1[a1].setPixmap(QPixmap(p1))
  v1[a1].setScaledContents(True)
  return v1[a1]
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap

def ql(self,tab0,p1,w,h,i):
  a1='self.lab' + str(i)
  
  v1 = {}  
  v1[a1] = QLabel(tab0)  
  v1[a1].setGeometry(0, 50, w, h)
  v1[a1].setPixmap(QPixmap(p1))
  v1[a1].setScaledContents(True)
  return v1[a1]
from PyQt5.QtWidgets import QTabWidget,QWidget
import pandas as pd
import path_def.pat1
from a__init__ import Btn,QLab
from c__init__ import para,nb,sval,sto1,start,plr,hor1
pic=[]

[pic.append(f"p{i}.png") for i in range(2)]

def initUI(self):
  self.resize(1600, 800)
  
  self.tabs = QTabWidget()
  self.tabs.setMovable(True)
  
  (self.tab0,self.tab1) = (QWidget(),QWidget())
  self.tabs.addTab(self.tab0,"Chart");self.tabs.addTab(self.tab1,"Help")         
  self.setCentralWidget(self.tabs)
  
  self.lab0=QLab(self,self.tab0,pic[0],1900,900,1,-150, -50)
  for i,con1 in enumerate((self.c0,self.c1)): Btn(self,self.tab0,con1,i,(i+1)*100-100,20)

  self.lab1=QLab(self,self.tab1,pic[1],1900,900,1,-150, -50)
  for i,con1 in enumerate((self.c2,self.c3)): i+=2; Btn(self,self.tab1,con1,i,(i+1)*100-100,20)
    
  # data 
  self.df='';self.sto2=[]   
  (self.para,self.nb,self.sval,self.sto1,self.start,self.plr)=(para,nb,sval,sto1,start,plr)
from PyQt5.QtWidgets import QTabWidget,QWidget
import pandas as pd
import path_def.pat1
from a__init__ import btn,ql
from c__init__ import para,nb,sval,sto1,start,plr,hor1
pic=[]

[pic.append(f"p{i}.png") for i in range(3)]

def initUI(self):
  self.resize(1600, 800)
  
  self.tabs = QTabWidget()
  self.tabs.setMovable(True)
  
  self.tab0,self.tab1 = QWidget(),QWidget()
  self.tabs.addTab(self.tab0,"Chart");self.tabs.addTab(self.tab1,"Help")         
  self.setCentralWidget(self.tabs)
  
  self.lab0=ql(self,self.tab0,pic[0],1900,900,1);self.lab0.move(-150, -50)
  for i,con1 in enumerate((self.c0,self.c1)): btn(self,self.tab0,con1,i)

  self.lab1=ql(self,self.tab1,pic[1],1900,900,1);self.lab1.move(-150, -50)
  self.lab1=ql(self,self.tab1,pic[2],200,150,2);self.lab1.move(1380, 630)
  for i,con1 in enumerate((self.c2,self.c3)): i+=2;btn(self,self.tab1,con1,i)
    
  # data 
  self.df='';self.sto2=[]   
  (self.para,self.nb,self.sval,self.sto1,self.start,self.plr)=(para,nb,sval,sto1,start,plr)
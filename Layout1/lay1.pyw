from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MW(QMainWindow):
    def __init__(self):
      super().__init__() ; self.initUI()

    from initUI1 import initUI
    from def1 import c0,c1,c2,c3

if __name__ == "__main__":
  app = QApplication(sys.argv)
  win = MW() ; win.show()
  sys.exit(app.exec_())
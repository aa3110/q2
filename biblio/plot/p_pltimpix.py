import matplotlib.pyplot as plt
import io
from PIL import Image
from PyQt5.QtGui import QPixmap
from PIL.ImageQt import ImageQt

def pltimpix(plt=''):
  buf = io.BytesIO(); plt.savefig(buf, format='png');buf.seek(0)
  pix=QPixmap.fromImage(ImageQt(Image.open(buf))) 
  return pix
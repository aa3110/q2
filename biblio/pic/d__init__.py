from pathlib import Path
import os

pic=[]
[pic.append(os.path.join(Path(os.path.abspath(os.path.dirname(__file__))+"\\"),f"p{i}.png")) for i in range(2)]
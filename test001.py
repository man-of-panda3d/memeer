from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import loadPrcFileData
from direct.gui.OnscreenImage import OnscreenImage
from panda3d.core import TransparencyAttrib
from direct.gui.DirectGui import *
import time
import json

from panda3d.core import *

with open('C:\ProgramData\VirtualBox\common\memeer\memeer\data.py') as json_file: serealized = json.load(json_file)

#serealized = [{'fncnm': 'screentext', 'text': ''}, {'fncnm': 'newmodel', 'params': {'animat': {'newobj': {'file': 'models/2dpics/narrator', 'gpoint': [0, 0, 0, 0, 0, 0, 300, 300, 300]}, 'frlen': 0}, 'qdets': {'locfrom': [], 'sttmts': [], 'locupto': [], 'locpos': [0, 0, 0, 0, 0, 0, 1, 1, 1], 'frames': 0}, 'scene': {'sceneid': '0', 'act': [0]}}}, {'fncnm': 'screentext', 'text': '"hello youong frinds"'}, {'fncnm': 'newmodel', 'params': {'animat': {'newobj': {'file': 'models/2dpics/narrator', 'gpoint': [0, 0, 0, 0, 0, 0, 300, 300, 300]}, 'frlen': 36}, 'qdets': {'locfrom': [], 'sttmts': ['"hello youong frinds"'], 'locupto': [], 'locpos': [], 'frames': 36}, 'scene': {'sceneid': '1', 'act': [1]}}}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'screentext', 'text': '"welcome to this animmation on far flung cltures of India"'}, {'fncnm': 'newmodel', 'params': {'animat': {'newobj': {'file': 'models/2dpics/narrator', 'gpoint': [0, 0, 0, 0, 0, 0, 300, 300, 300]}, 'frlen': 72}, 'qdets': {'locfrom': [], 'sttmts': ['"welcome to this animmation on far flung cltures of India"'], 'locupto': [], 'locpos': [], 'frames': 72}, 'scene': {'sceneid': '2', 'act': [2]}}}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'screentext', 'text': '"My name is Ahmad Balti and today, I will tell you about my Balti ( pronounced बलटी)  people"'}, {'fncnm': 'newmodel', 'params': {'animat': {'newobj': {'file': 'models/2dpics/narrator', 'gpoint': [0, 0, 0, 0, 0, 0, 300, 300, 300]}, 'frlen': 72}, 'qdets': {'locfrom': [], 'sttmts': ['"My name is Ahmad Balti and today, I will tell you about my Balti ( pronounced बलटी)  people"'], 'locupto': [], 'locpos': [], 'frames': 72}, 'scene': {'sceneid': '3', 'act': [3]}}}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'screentext', 'text': ''}, {'fncnm': 'newmodel', 'params': {'animat': {'newobj': {'file': 'models/2dpics/indiamap', 'gpoint': [0, 0, 0, 0, 0, 0, 300, 300, 300]}, 'frlen': 12}, 'qdets': {'locfrom': [], 'sttmts': [], 'locupto': [], 'locpos': [0, 0, 0, 0, 0, 0, 1, 1, 1], 'frames': 12}, 'scene': {'sceneid': '4', 'act': [4]}}}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'screentext', 'text': ''}, {'fncnm': 'newmodel', 'params': {'animat': {'newobj': {'file': 'models/2dpics/narrator', 'gpoint': [0, 0, 0, 0, 0, 0, 300, 300, 300]}, 'frlen': 0}, 'qdets': {'locfrom': [], 'sttmts': [], 'locupto': [], 'locpos': [0, 0, 0, 0, 0, 0, 0, 0, 0], 'frames': 0}, 'scene': {'sceneid': '5', 'act': [5]}}}, {'fncnm': 'screentext', 'text': '"first, some basics"'}, {'fncnm': 'newmodel', 'params': {'animat': {'newobj': {'file': 'models/2dpics/narrator', 'gpoint': [0, 0, 0, 0, 0, 0, 300, 300, 300]}, 'frlen': 36}, 'qdets': {'locfrom': [], 'sttmts': ['"first, some basics"'], 'locupto': [], 'locpos': [], 'frames': 36}, 'scene': {'sceneid': '6', 'act': [6]}}}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'screentext', 'text': '"Geography"'}, {'fncnm': 'newmodel', 'params': {'animat': {'newobj': {'file': 'models/2dpics/narrator', 'gpoint': [0, 0, 0, 0, 0, 0, 300, 300, 300]}, 'frlen': 12}, 'qdets': {'locfrom': [], 'sttmts': ['"Geography"'], 'locupto': [], 'locpos': [], 'frames': 12}, 'scene': {'sceneid': '7', 'act': [7]}}}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'screentext', 'text': ''}, {'fncnm': 'screentext', 'text': '"there i am... there on the top of mountains of mighty himalaya, some 3km above sea level"'}, {'fncnm': 'newmodel', 'params': {'animat': {'newobj': {'file': 'models/2dpics/narrator', 'gpoint': [0, 0, 0, 0, 0, 0, 300, 300, 300]}, 'frlen': 96}, 'qdets': {'locfrom': [], 'sttmts': ['"there i am... there on the top of mountains of mighty himalaya, some 3km above sea level"'], 'locupto': [], 'locpos': [], 'frames': 96}, 'scene': {'sceneid': '9', 'act': [9]}}}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'screentext', 'text': '"and now a brief history"'}, {'fncnm': 'newmodel', 'params': {'animat': {'newobj': {'file': 'models/2dpics/narrator', 'gpoint': [0, 0, 0, 0, 0, 0, 300, 300, 300]}, 'frlen': 36}, 'qdets': {'locfrom': [], 'sttmts': ['"and now a brief history"'], 'locupto': [], 'locpos': [], 'frames': 36}, 'scene': {'sceneid': '10', 'act': [10]}}}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'screentext', 'text': ''}, {'fncnm': 'newmodel', 'params': {'animat': {'newobj': {'file': 'models/2dpics/indiamap', 'gpoint': [0, 0, 0, 0, 0, 0, 300, 300, 300]}, 'frlen': 0}, 'qdets': {'locfrom': [], 'sttmts': [], 'locupto': [], 'locpos': [0, 1, 0, 0, 0, 0, 0, 0, 0], 'frames': 0}, 'scene': {'sceneid': '11', 'act': [11]}}}, {'fncnm': 'screentext', 'text': ''}, {'fncnm': 'newmodel', 'params': {'animat': {'newobj': {'file': 'models/2dpics/SEAMap', 'gpoint': [0, 0, 0, 0, 0, 0, 300, 300, 300]}, 'frlen': 0}, 'qdets': {'locfrom': [], 'sttmts': [], 'locupto': [], 'locpos': [0, 0, 0, 0, 0, 0, 1, 1, 1], 'frames': 0}, 'scene': {'sceneid': '12', 'act': [12]}}}, {'fncnm': 'screentext', 'text': '"Balti people have been carrying the legacy of Tibet since atleast 600AD. The overall geneology of this group contain Tibet, Laddakh and Mongolan ancestry."'}, {'fncnm': 'newmodel', 'params': {'animat': {'newobj': {'file': 'models/2dpics/narrator', 'gpoint': [0, 0, 0, 0, 0, 0, 300, 300, 300]}, 'frlen': 120}, 'qdets': {'locfrom': [], 'sttmts': ['"Balti people have been carrying the legacy of Tibet since atleast 600AD. The overall geneology of this group contain Tibet, Laddakh and Mongolan ancestry."'], 'locupto': [], 'locpos': [], 'frames': 120}, 'scene': {'sceneid': '13', 'act': [13]}}}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'screentext', 'text': '"Around 600 years back, a persian by name of Mir Sayyid Ali bought Shia branch of Islam to the region."'}, {'fncnm': 'newmodel', 'params': {'animat': {'newobj': {'file': 'models/2dpics/narrator', 'gpoint': [0, 0, 0, 0, 0, 0, 300, 300, 300]}, 'frlen': 120}, 'qdets': {'locfrom': [], 'sttmts': ['"Around 600 years back, a persian by name of Mir Sayyid Ali bought Shia branch of Islam to the region."'], 'locupto': [], 'locpos': [], 'frames': 120}, 'scene': {'sceneid': '14', 'act': [14]}}}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'screentext', 'text': '"Troughout history, this area have been ruled by Rajas of Hunza, Dogra, and part of the princely state of Jammu and Kashmir rulers."'}, {'fncnm': 'newmodel', 'params': {'animat': {'newobj': {'file': 'models/2dpics/narrator', 'gpoint': [0, 0, 0, 0, 0, 0, 300, 300, 300]}, 'frlen': 120}, 'qdets': {'locfrom': [], 'sttmts': ['"Troughout history, this area have been ruled by Rajas of Hunza, Dogra, and part of the princely state of Jammu and Kashmir rulers."'], 'locupto': [], 'locpos': [], 'frames': 120}, 'scene': {'sceneid': '15', 'act': [15]}}}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'screentext', 'text': '"In the year 1947, following the Pakistani army invasion, Pakistani army captured our land, which was partially freed in 1971 war."'}, {'fncnm': 'newmodel', 'params': {'animat': {'newobj': {'file': 'models/2dpics/narrator', 'gpoint': [0, 0, 0, 0, 0, 0, 300, 300, 300]}, 'frlen': 120}, 'qdets': {'locfrom': [], 'sttmts': ['"In the year 1947, following the Pakistani army invasion, Pakistani army captured our land, which was partially freed in 1971 war."'], 'locupto': [], 'locpos': [], 'frames': 120}, 'scene': {'sceneid': '16', 'act': [16]}}}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'screentext', 'text': ''}, {'fncnm': 'newmodel', 'params': {'animat': {'newobj': {'file': 'models/2dpics/narrator', 'gpoint': [0, 0, 0, 0, 0, 0, 300, 300, 300]}, 'frlen': 0}, 'qdets': {'locfrom': [], 'sttmts': [], 'locupto': [], 'locpos': [0, 0, 0, 0, 0, 0, 1, 1, 1], 'frames': 0}, 'scene': {'sceneid': '17', 'act': [17]}}}, {'fncnm': 'screentext', 'text': ''}, {'fncnm': 'newmodel', 'params': {'animat': {'newobj': {'file': 'models/2dpics/SEAMap', 'gpoint': [0, 0, 0, 0, 0, 0, 300, 300, 300]}, 'frlen': 0}, 'qdets': {'locfrom': [], 'sttmts': [], 'locupto': [], 'locpos': [0, 0, 0, 0, 0, 0, 0, 0, 0], 'frames': 0}, 'scene': {'sceneid': '18', 'act': [18]}}}, {'fncnm': 'screentext', 'text': '"Ok, so enough boring study time... let us move to the cool things you may like here :) "'}, {'fncnm': 'newmodel', 'params': {'animat': {'newobj': {'file': 'models/2dpics/narrator', 'gpoint': [0, 0, 0, 0, 0, 0, 300, 300, 300]}, 'frlen': 120}, 'qdets': {'locfrom': [], 'sttmts': ['"Ok, so enough boring study time... let us move to the cool things you may like here :) "'], 'locupto': [], 'locpos': [], 'frames': 120}, 'scene': {'sceneid': '19', 'act': [19]}}}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}, {'fncnm': 'passblank'}]
modlist = []

def logallposes ():
	print (base.camera.getPos())
	print (base.camera.getHpr())
	for obj in modlist:
		print (obj['file'], obj['model'].getTightBounds())

def setmodelpos (actor, posset):
	basepos = [0, 0, 0, 0, 0, 0, .1, .1, .1]
	print ("Setting new posset: ", posset)
	for pos in posset:
		if pos == []: continue
		for ix in range(0,6):
			if len(pos) >= ix: basepos[ix] = basepos[ix] + float(pos[ix])
		for ix in range(6,9):
			if len(pos) >= ix: basepos[ix] = basepos[ix] * float(pos[ix])
	print (actor, basepos)
	actor.setPos(basepos[0], basepos[1], basepos[2])
	actor.setHpr(basepos[3], basepos[4], basepos[5])
	actor.setScale(basepos[6], basepos[7], basepos[8])
	print (actor, actor.getTightBounds())
	return 1

def checkformodel (modfile):
	for mno, model in enumerate(modlist):
		if model['file'] == modfile: return mno
	return -1

def newactor (animat, qdets):
	modid = checkformodel (animat['newobj']['file'])
	if modid == -1:
		model = Actor(animat['newobj']['file'], animat['newobj']['acts'])
		setmodelpos (model, [animat['newobj']['gpoint'], qdets['locpos'], qdets['locfrom']])
		model.reparentTo(render)
		modlist.append({'file': animat['newobj']['file'], 'model': model, 'render': 1})
		modid = len(modlist)-1
	return modid

def newmodel (animat, qdets):
	modid = checkformodel (animat['newobj']['file'])
	if modid == -1:
		model = loader.loadModel(animat['newobj']['file'])
		setmodelpos (model, [animat['newobj']['gpoint'], qdets['locpos'], qdets['locfrom']])
		model.reparentTo(render)
		modlist.append({'file': animat['newobj']['file'], 'model': model, 'render': 1})
		modid = len(modlist)-1
	elif 'locpos' in qdets and len(qdets['locpos']) > 2:
		setmodelpos (modlist[modid]['model'], [animat['newobj']['gpoint'], qdets['locpos'], qdets['locfrom']])
	return modid

def actorposes (animat, frame):
	modid = checkformodel (animat['model'])
	modlist[modid]['model'].pose (animat['action'], frame)
	if 'lochpr' in animat:
		setmodelpos (modlist[modid]['model'], [animat['lochpr']])
	return 1

def screentext (text):
	textObject.text = text
	return 1

def passblank ():
	return 0

def camerasetup (poshpr):
	base.camera.setPos(float(poshpr[0]), float(poshpr[1]), float(poshpr[2]))
	base.camera.setHpr(float(poshpr[3]), float(poshpr[4]), float(poshpr[5]))
	return 1

def defaultTask(task):
	print('Current frame: '+str(task.frame))
	if task.frame >= len(serealized): return Task.done
	scenef = serealized[task.frame]
	if scenef['fncnm'] == 'camerasetup': camerasetup(scenef['params'])
	if scenef['fncnm'] == 'newmodel': newmodel(scenef['params']['animat'], scenef['params']['qdets'])
	if scenef['fncnm'] == 'newactor': newactor(scenef['params']['animat'], scenef['params']['qdets'])
	if scenef['fncnm'] == 'actorposes': actorposes(scenef['params'], scenef['frame'])
	if scenef['fncnm'] == 'screentext': screentext(scenef['text'])
	if scenef['fncnm'] not in ['actorposes', 'passblank']:
		logallposes ()
	return Task.cont

from pandac.PandaModules import ClockObject
FPS = 30
globalClock = ClockObject.getGlobalClock()
globalClock.setMode(ClockObject.MLimited)
globalClock.setFrameRate(FPS)

ShowBase()
base.disableMouse()
camera.setPos(0, -120, 10)
camera.setHpr(0, 0, 0)
textObject = OnscreenText(text=" ", pos=(-1.2, 0.9), scale=0.08, align=0, wordwrap=40)
taskMgr.add(defaultTask, "defaultTask")
base.run()
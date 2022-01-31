from ij import IJ, ImagePlus
from ij.process import FloatProcessor, ImageProcessor
from ij.gui import Roi, PolygonRoi, GenericDialog, TextRoi, NonBlockingGenericDialog
from ij.io import OpenDialog, FileSaver
import re
from java.awt import Color
from javax.swing import JScrollPane, JPanel, JComboBox, JLabel, JFrame, JTextArea
import javax
import time
import sys
import os, shutil, glob

import ij.io 
import uuid
# overwrites filenames in the selected folder (source), it does currently print the wholefile name. 
OUT = open("/Users/JohnSargeant/Desktop/filenames_1.csv", "a")
source = IJ.getDirectory("choose source")


for filename in os.listdir(source):
	if filename.endswith('.tif'):
		name = str(uuid.uuid4())
		print(filename,name)
		save_stdout = sys.stdout
		sys.stdout = OUT
		print filename, ",",name
		sys.stdout = save_stdout
		dst = name + ".tif"
		src = source + filename
		dst = source + dst
		os.rename(src,dst)
	
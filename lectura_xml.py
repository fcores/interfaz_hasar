import sys
import numpy as np
#import matplotlib.pyplot as plt
import shutil
from PIL import Image
import os
import PIL
#from bs4 import BeautifulSoup as bs
import requests
#from bs4 import BeautifulSoup as bs
import requests
import argparse
import time
from scipy import ndimage
from os import walk
import sys
from datetime import datetime
import os
from PIL import ImageTk, Image
import pythoncom
import threading
import os, sys, stat
from getpass import getuser
import ctypes
import os
from xml.etree.ElementTree import parse
from os import remove
from bs4 import BeautifulSoup
from zipfile import ZipFile

def lector(inicio,fin):
    
    # puesto_conexion=[{"102":"172.18.2.102"},{"103","172.18.2.103"},
    # {"104":"172.18.2.104"},{"105":"172.18.2.105"},{"106":"172.18.2.24"},
    # {"107":"172.19.2.107"},{"101":"192.168.4.101"},{"108":"172.19.2.108"},
    # {"120":"172.19.2.120"},{"109":"172.24.2.209"},{"110":"172.24.2.210"},
    # {"111":"172.24.2.211"},{"112":"172.24.2.212"},{"113":"172.24.2.213"},
    # {"114":"172.24.2.214"},{"115":"172.24.2.215"},{"116":"172.24.2.216"},
    # {"117":"172.24.2.217"}]
    
    puesto_conexion=[{"106":"172.18.2.24"},{"107":"172.19.2.107"}]

    for i in puesto_conexion:
        for p in i.keys():
            puesto=p
        for h in i.values():
            ip=h
        os.mkdir("C:/Users/fcores/Desktop/reporte_afip/" + puesto )
        ruta="C:/Users/fcores/Desktop/reporte_afip/" + puesto + ".zip"
        headers={"Content-Type":"text/xml"}
        response = requests.post("http://" + ip + "/afip.zip?DESDE=" + str(inicio) + "&HASTA=" + str(fin),auth=("",'9999'),headers=headers)
        print(response.status_code)
        with open(ruta,'wb') as file:
            for entrega in response.iter_content():
                file.write(entrega)
        with ZipFile(ruta, 'r') as zip:
            zip.extractall("C:/Users/fcores/Desktop/reporte_afip/" + puesto) 

    
lector(211208,211212)  

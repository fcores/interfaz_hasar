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

def lector():
    
    # puesto_conexion=[{"102":"172.18.2.102"},{"103","172.18.2.103"},
    # {"104":"172.18.2.104"},{"105":"172.18.2.105"},{"106":"172.18.2.24"},
    # {"107":"172.19.2.107"},{"101":"192.168.4.101"},{"108":"172.19.2.108"},
    # {"120":"172.19.2.120"},{"109":"172.24.2.209"},{"110":"172.24.2.210"},
    # {"111":"172.24.2.211"},{"112":"172.24.2.212"},{"113":"172.24.2.213"},
    # {"114":"172.24.2.214"},{"115":"172.24.2.215"},{"116":"172.24.2.216"},
    # {"117":"172.24.2.217"}]
    
    puesto_conexion=[{"106":"172.18.2.24"},{"113":"172.24.2.213"}]

    for i in puesto_conexion:
        ruta="C:/Users/fcores/Desktop/reporte_afip/" + i.keys() + ".zip"
        headers={"Content-Type":"text/xml"}
        response = requests.post("http://" + i.values() + "/afip.zip?DESDE=211208&HASTA=211212",auth=("",'9999'),headers=headers)
        print(response.status_code)
        with open(ruta,'wb') as file:
            for entrega in response.iter_content():
                file.write(entrega)

    
lector()  

import sys
import numpy as np
import matplotlib.pyplot as plt
import shutil
from PIL import Image
import os
import PIL
from bs4 import BeautifulSoup as bs
import requests
from bs4 import BeautifulSoup as bs
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

def lector(entreg,ruta,dia,farmacia):
    ruta="U:/Farmacias/DOKA_TICKETS_COBERTURA_PARCIAL/2021"
    rutahtml=ruta+"/"+str(entreg)+".html"
    if farmacia=="GÜEMES": ######URL GUEMES2#######
        url="172.19.2.107"
    elif farmacia=="PUEYRREDÓN": ######URL PUEYRREDON2#######
        url="172.18.2.24"
        
    headers={"Content-Type":"text/xml"}
    response = requests.get("http://" + url + "/verdocs.html?FECHA=" + str(dia) + "&VER=Ver",auth=("",'9999'))
    soup = BeautifulSoup(response.text, "xml")
    etiquetas=soup.findAll("td",class_="RowRight")
    id=etiquetas[0].text
    r="no_descargado"

    for i in range(0,200):
        try:
            headers={"Content-Type":"text/xml"}
            response = requests.get("http://" + url + "/documento.xml?ZETA=" + str(id) + "&DOCID=" + str(i),auth=("",'9999'))
            soup = BeautifulSoup(response.text, "xml")
            etiqueta=soup.findAll("Texto")
            entrega=str(etiqueta[1].string)
            if "Receta" in entrega and entrega[8]=="8":
                if entrega[8:16]==entreg:
                    response = requests.get("http://" + url + "/verdoc.html?ZETA=" + str(id) + "&DOCID=" + str(i),auth=("",'9999'))
                    with open(rutahtml,'wb') as file:
                        for entrega in response.iter_content():
                            file.write(entrega)
                        r="descargado"
                    break
                else:
                    continue
            else:
                continue
        except: 
            continue
    return r


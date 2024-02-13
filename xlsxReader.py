import csv
#import sys
#sys.path.append("C:\\Users\\davil\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python311\\site-packages")
#import openpyxl
#opxl = openpyxl
import tkinter as tk
from tkinter import filedialog
import trans as tr

def translitCSVFile(file):
    
    fw = open('_transliterated.csv', 'w', newline='')
    reader = csv.reader(file,delimiter=';')
    writer = csv.writer(fw,delimiter=';')
    brow = list()
    table = list()
    i = 0

    for row in reader:
        for cell in row:
            brow.insert(i, tr.FnTranslit(cell))
            i += 1
        table.append(brow)
        brow = list()

    writer.writerows(table)


def translitXLSXFile(file):
    return NotImplemented
    fw = open('_transliterated.csv', 'w', newline='')
    reader = csv.reader(file,delimiter=';')
    writer = csv.writer(fw,delimiter=';')
    brow = list()
    table = list()
    i = 0

    for row in reader:
        for cell in row:
            brow.insert(i, tr.FnTranslit(cell))
            i += 1
        table.append(brow)
        brow = list()

    writer.writerows(table)

def translitJSON(str):
    return tr.FnTranslit(str)

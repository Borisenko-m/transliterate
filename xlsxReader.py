import csv
#import openpyxl as xl

import trans as tr

def replaceName(name: str):
    return f'{name.removesuffix('.csv')}_transliterated.csv'

def translitText(name: str, data: str):
    data = tr.FnTranslit(data)
    fw = open(replaceName(name), 'w', newline='')
    fw.write(data)
    fw.close()


def translitCSVFile(name: str, file: list):
    
    fw = open(replaceName(name), 'w', newline='')
    reader = csv.reader(file, delimiter=';')
    writer = csv.writer(fw, delimiter=';')
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
    return "ok"


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

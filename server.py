import sys
sys.path.append("C:\\Users\\davil\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python311\\site-packages")
import xlsxReader
import uuid
from fastapi import FastAPI, Body, status, UploadFile, File
from fastapi.responses import JSONResponse, FileResponse, Response

app = FastAPI()

@app.post('/api/transliterateCSV')
def transliterate(file: UploadFile):
    
    res = xlsxReader.translitCSVFile(file)
    return status.HTTP_200_OK

@app.post('/api/transliterateXLSX')
def transliterate(file: UploadFile):
    res = xlsxReader.translitXLSXFile(file)
    return status.HTTP_200_OK

@app.post('/api/transliterateJSON')
def transliterate(str):
    res = xlsxReader.translitJSON(str)
    return status.HTTP_200_OK

    
#import sys
#sys.path.append("C:\\Users\\davil\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python311\\site-packages")
import chardet
import xlsxReader
from fastapi import FastAPI, UploadFile
from fastapi.responses import HTMLResponse 
import uvicorn 

app = FastAPI()
class Api(object):
   
    def __init__(self, app: FastAPI):
        self.app = app
    
    @app.post("/api/translitCSVFile/")
    async def api_translitCSVFile(files: list[UploadFile]):

        encoding: str = ""
        lines = list()

        for file in files: 
            for line in file.file.readlines():
                if encoding == "": encoding = encoding = chardet.detect(line)['encoding']
                lines.append(line.decode(encoding))
            xlsxReader.translitCSVFile(file.filename,lines)
            encoding = ""
            lines.clear()

        return "ok"
    
    # Not implemented:
    @app.post("/api/translitXLSXFile/")
    async def api_translitXLSXFile(files: list[UploadFile]):

        encoding: str = ""
        lines = list()

        for file in files: 
            for line in file.file.readlines():
                if encoding == "": 
                    encoding = encoding = chardet.detect(line)['encoding']
                
                lines.append(line.decode(encoding))
            
            xlsxReader.translitCSVFile(file.filename,lines)
            encoding = ""
            lines.clear()

        return "ok"
    

    @app.get("/")
    async def main():
        def showMethod(method):
            return  f"""
                    <div><h4>{method}</h4>
                    <form action="{method}" enctype="multipart/form-data" method="post">
                    <input name="files" type="file" multiple>
                    <input type="submit">
                    </form>
                    </div>
                    """
        content = ''
        for method in dir(Api(app)):
            if method.startswith('api_'):
                content += ''.join(showMethod('api/' + method.removeprefix('api_')))
        
        return HTMLResponse(f"<body>{content}</body>")

    @app.post('/api/transliterateJSON')
    def api_transliterateJSON(file):
        return xlsxReader.translitCSVFile(file)


if __name__ == "__main__":
    config = uvicorn.Config("server:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    api = Api(app)
    server.run()
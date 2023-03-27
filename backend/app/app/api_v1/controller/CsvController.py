import os
import sys

path = os.environ['FILE_PATH']
sys.path.append(path)

from fastapi import APIRouter
from fastapi.responses import Response, StreamingResponse, FileResponse
from fastapi.requests import Request
from app.core.business.abstracts.CsvService import CsvService
from typing import List

csvroutes = APIRouter()
csvService = CsvService()


@csvroutes.post("/")
def write_csv_data_with_responseClass(request: Request) -> Response:
    data: List[str] = request.data
    file_name = request.data.get("filename")
    headers = {'Content-Disposition': f'attachment; filename='{file_name}'.csv'}
    response =  Response(content=data, status_code=status.HTTP_200_OK, headers=headers, media_type='text/csv')
    csvService.writeCsv(response, data)

@csvroutes.post("/")
def write_large_streaming_csv_view(request) -> StreamingResponse:
    data: int = request.data or 65536
    file_name = None
    headers = {'Content-Disposition': f'attachment; filename="{file_name}.csv"'}
    media_type = "text/csv"
    writer = csvService.stream_csv_view(data)
    return StreamingHttpResponse((writer.writerow(row) for row in rows), media_type="text/csv",headers=headers)

@csvroutes.post("/")
def write_csv_data_with_fileResponse():
    file_path = None
    headers = {}
    filename = None
    media_type = 'text/csv'
    return FileResponse(path=file_path, headers=headers, media_type=media_type, filename=filename)

@csvroutes.post("/")
def write_csv_data_with_streamResponse():
    file_path = ""
    def iterfile():
        with open(file_path, mode='rb') as file:
            yield from file
    return StreamingResponse(iterfile(), media_type="text/csv")


@csvroutes.get("/")
def get_csv_data_file_download():
    file_path = None
    headers = {'Content-Disposition': f'attachment; filename='{name + "_" + lastname}'.csv'}
    filename = None
    media_type = None
    return FileResponse(path=file_path, headers=headers, media_type=media_type, filename=filename)


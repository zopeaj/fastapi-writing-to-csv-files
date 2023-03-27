import os
import sys

path = os.environ['FILE_PATH']
sys.path.append(path)

from fastapi import APIRouter
from app.api_v1.controller.CsvController import csvroutes

api_router = APIRouter()

api_router.include_router(csvroutes, prefix="/api/v1/csv/", tags=["csv-reader-writer"])


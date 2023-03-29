import os
import sys

path = os.environ['FILE_PATH']
sys.path.append(path)

from fastapi import APIRouter
from app.api_1.routes import api_router

app = FastAPI(title="Writing To Csv")
app.include_router(api_router, prefix="api/v1/")





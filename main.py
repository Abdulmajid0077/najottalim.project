from fastapi import FastAPI
from database import *

app = FastAPI(title="NAjottalim Backend")
Base.metadata.create_all(bind=engine)
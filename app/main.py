from fastapi import FastAPI 
from .routers import user
from . import models
from .database import engine

# bootstrap
app = FastAPI()
# db init
models.Base.metadata.create_all(bind=engine)
# routers
app.include_router(user.router)

from typing import List
from urllib import response
from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadate.create_all(bind=engine)

app =FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#read
@app.get('/Remind/plant', response_model= List[schemas.PlantMsg])
async def Get_PlantMsg(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    plantMsg = crud.getPlantMsg(db,skip=skip,limit=limit)
    return plantMsg

@app.get('/Remind/aler', response_model= List[schemas.AlerMsg])
async  def Get_AlerMsg(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    alerMsg = crud.getAlerMsg(db,skip=skip,limit=limit)
    return alerMsg

#create
@app.post('/Remind/plant',response_model=schemas.PlantMsg)
async  def PlantMsg(plantMsg: schemas.PlantMsg, db: Session = Depends(get_db)):
    return crud.create_AlerMsg(db=db, plantMsg=plantMsg)


@app.post('/Remind/aler',response_model=schemas.AlerMsg)
async  def AlerMsg(alerMsg: schemas.AlerMsg , db: Session = Depends(get_db)):
    return crud.create_AlerMsg(db=db, alerMsg=alerMsg)


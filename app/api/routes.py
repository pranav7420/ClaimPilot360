from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import schemas
from app.crud import crud
from app.db.database import SessionLocal
from typing import List
import logging

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/policies/", response_model=schemas.Policy)
def create_policy(policy: schemas.PolicyCreate, db: Session = Depends(get_db)):
    logging.info("Sombody tried to hit createPolices endpoint.")
    logging.info("Made some Changes after review commnets.")
    return crud.create_policy(db, policy)

@router.get("/policies/", response_model=List[schemas.Policy])
def read_policies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_policies(db, skip=skip, limit=limit)

@router.get("/policies/{policy_id}", response_model=schemas.Policy)
def read_policy(policy_id: int, db: Session = Depends(get_db)):
    db_policy = crud.get_policy(db, policy_id)
    if db_policy is None:
        raise HTTPException(status_code=404, detail="Policy not found")
    return db_policy

@router.post("/claims/", response_model=schemas.Claim)
def create_claim(claim: schemas.ClaimCreate, db: Session = Depends(get_db)):
    return crud.create_claim(db, claim)

@router.get("/claims/", response_model=List[schemas.Claim])
def read_claims(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_claims(db, skip=skip, limit=limit)

@router.get("/claims/{claim_id}", response_model=schemas.Claim)
def read_claim(claim_id: int, db: Session = Depends(get_db)):
    db_claim = crud.get_claim(db, claim_id)
    if db_claim is None:
        raise HTTPException(status_code=404, detail="Claim not found")
    return db_claim
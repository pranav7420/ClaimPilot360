from sqlalchemy.orm import Session
from app.models.models import Policy, Claim
from app.schemas.schemas import PolicyCreate, ClaimCreate


def create_policy(db: Session, policy: PolicyCreate):
    db_policy = Policy(**policy.dict())
    
    db.add(db_policy)
    db.commit()
    db.refresh(db_policy)
    return db_policy

def get_policies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Policy).offset(skip).limit(limit).all()

def get_policy(db: Session, policy_id: int):
    return db.query(Policy).filter(Policy.id == policy_id).first()

def create_claim(db: Session, claim: ClaimCreate):
    db_claim = Claim(**claim.dict())
    db.add(db_claim)
    db.commit()
    db.refresh(db_claim)
    return db_claim

def get_claims(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Claim).offset(skip).limit(limit).all()

def get_claim(db: Session, claim_id: int):
    return db.query(Claim).filter(Claim.id == claim_id).first()
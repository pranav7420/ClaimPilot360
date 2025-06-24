from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PolicyBase(BaseModel):
    policy_number: str
    holder_name: str
    premium: float
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

class PolicyCreate(PolicyBase):
    pass

class Policy(PolicyBase):
    id: int

    class Config:
        orm_mode = True

class ClaimBase(BaseModel):
    policy_id: int
    claim_amount: float
    claim_date: Optional[datetime] = None
    status: Optional[str] = "Pending"

class ClaimCreate(ClaimBase):
    pass

class Claim(ClaimBase):
    id: int

    class Config:
        orm_mode = True
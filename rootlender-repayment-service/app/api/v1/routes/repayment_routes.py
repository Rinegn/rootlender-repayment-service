from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import SessionLocal
from app.models.repayment import Repayment
from app.schemas.repayment import RepaymentCreate, RepaymentResponse
from app.services.repayment_engine import RepaymentEngine

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=RepaymentResponse)
def create_repayment(payload: RepaymentCreate, db: Session = Depends(get_db)):
    repayment = Repayment(**payload.model_dump())
    db.add(repayment)
    db.commit()
    db.refresh(repayment)
    return repayment

@router.get("/{repayment_id}", response_model=RepaymentResponse)
def get_repayment(repayment_id: int, db: Session = Depends(get_db)):
    repayment = db.query(Repayment).filter(Repayment.id == repayment_id).first()
    if not repayment:
        raise HTTPException(status_code=404, detail="Repayment not found")
    return repayment

from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal

class RepaymentBase(BaseModel):
    loan_id: int
    installment_number: int
    amount_due: Decimal
    due_date: datetime

class RepaymentCreate(RepaymentBase):
    pass

class RepaymentUpdate(BaseModel):
    amount_paid: Decimal
    status: str

class RepaymentResponse(RepaymentBase):
    id: int
    amount_paid: Decimal
    status: str
    paid_at: datetime | None

    class Config:
        from_attributes = True

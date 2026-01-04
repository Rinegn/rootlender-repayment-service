from sqlalchemy import Column, Integer, Numeric, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database.base import Base

class Repayment(Base):
    __tablename__ = "repayments"

    id = Column(Integer, primary_key=True, index=True)
    loan_id = Column(Integer, nullable=False, index=True)
    installment_number = Column(Integer, nullable=False)
    amount_due = Column(Numeric(10, 2), nullable=False)
    amount_paid = Column(Numeric(10, 2), default=0)
    status = Column(String(20), nullable=False, default="pending")
    due_date = Column(DateTime, nullable=False)
    paid_at = Column(DateTime)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

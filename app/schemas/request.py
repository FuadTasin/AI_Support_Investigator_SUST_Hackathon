from typing import List, Optional
from pydantic import BaseModel, Field


class Transaction(BaseModel):
    transaction_id: str = Field(..., description="Unique transaction ID")
    amount: float = Field(..., gt=0)
    transaction_type: str = Field(..., description="transfer/payment/cash_in/etc.")
    status: str = Field(..., description="completed/failed/pending")
    timestamp: str
    counterparty: Optional[str] = None


class AnalyzeTicketRequest(BaseModel):
    ticket_id: str
    complaint: str
    language: str = "en"
    channel: str = "api"
    user_type: str = "customer"

    transaction_history: List[Transaction]
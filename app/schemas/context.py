from typing import List, Optional
from pydantic import BaseModel

from app.schemas.request import Transaction


class AnalysisContext(BaseModel):
    # ==========================
    # Original Request
    # ==========================

    ticket_id: str
    complaint: str
    language: str
    channel: str
    user_type: str
    transaction_history: List[Transaction]

    # ==========================
    # AI Extraction Output
    # ==========================

    intent: str = "other"

    extracted_amount: Optional[float] = None

    transaction_type: Optional[str] = None

    mentioned_time: Optional[str] = None

    fraud: bool = False

    confidence: float = 0.0

    # ==========================
    # Investigation
    # ==========================

    matched_transaction: Optional[Transaction] = None

    evidence_verdict: str = "insufficient_data"

    case_type: str = "other"

    severity: str = "low"

    department: str = "customer_support"

    human_review_required: bool = False

    # ==========================
    # AI Generated Outputs
    # ==========================

    agent_summary: str = ""

    recommended_next_action: str = ""

    customer_reply: str = ""

    # ==========================
    # Debug
    # ==========================

    reason_codes: List[str] = []
from typing import Optional
from pydantic import BaseModel


class AnalyzeTicketResponse(BaseModel):
    ticket_id: str

    relevant_transaction_id: Optional[str]

    evidence_verdict: str

    case_type: str

    severity: str

    department: str

    agent_summary: str

    recommended_next_action: str

    customer_reply: str

    human_review_required: bool
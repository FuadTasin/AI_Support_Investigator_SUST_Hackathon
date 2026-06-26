from fastapi import APIRouter

from app.schemas.request import AnalyzeTicketRequest
from app.schemas.context import AnalysisContext

from app.core.investigation_engine import InvestigationEngine
from app.builders.response_builder import ResponseBuilder

router = APIRouter()

engine = InvestigationEngine()
builder = ResponseBuilder()


@router.get("/health")
async def health():
    return {
        "status": "ok"
    }


@router.post("/analyze-ticket")
async def analyze_ticket(request: AnalyzeTicketRequest):

    context = AnalysisContext(
        ticket_id=request.ticket_id,
        complaint=request.complaint,
        language=request.language,
        channel=request.channel,
        user_type=request.user_type,
        transaction_history=request.transaction_history
    )

    context = engine.run(context)

    return builder.build(context)
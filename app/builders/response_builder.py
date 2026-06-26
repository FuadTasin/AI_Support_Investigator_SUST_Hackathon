from app.schemas.context import AnalysisContext
from app.schemas.response import AnalyzeTicketResponse


class ResponseBuilder:

    def build(
        self,
        context: AnalysisContext
    ):

        return AnalyzeTicketResponse(

            ticket_id=context.ticket_id,

            relevant_transaction_id=(
                context.matched_transaction.transaction_id
                if context.matched_transaction
                else None
            ),

            evidence_verdict=context.evidence_verdict,

            case_type=context.case_type,

            severity=context.severity,

            department=context.department,

            agent_summary=context.agent_summary,

            recommended_next_action=context.recommended_next_action,

            customer_reply=context.customer_reply,

            human_review_required=context.human_review_required
        )
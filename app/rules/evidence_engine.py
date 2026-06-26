from app.schemas.context import AnalysisContext


class EvidenceEngine:

    def process(self, context: AnalysisContext):

        txn = context.matched_transaction

        if txn is None:

            context.evidence_verdict = "insufficient_data"

            return context

        if context.fraud:

            context.evidence_verdict = "consistent"

            return context

        if txn.status.lower() == "completed":

            context.evidence_verdict = "consistent"

        elif txn.status.lower() == "failed":

            context.evidence_verdict = "consistent"

        else:

            context.evidence_verdict = "inconsistent"

        return context
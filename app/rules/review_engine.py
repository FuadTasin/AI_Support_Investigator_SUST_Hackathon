from app.schemas.context import AnalysisContext


class ReviewEngine:

    def process(self, context: AnalysisContext):

        review = False

        if context.severity in [

            "high",

            "critical"

        ]:

            review = True

        if context.fraud:

            review = True

        if context.evidence_verdict != "consistent":

            review = True

        if context.confidence < 0.70:

            review = True

        context.human_review_required = review

        return context
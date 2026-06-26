from app.schemas.context import AnalysisContext


class SeverityEngine:

    def process(self, context: AnalysisContext):

        if context.fraud:
            context.severity = "critical"
            return context

        severity_map = {

            "wrong_transfer": "high",

            "payment_issue": "medium",

            "double_charge": "medium",

            "complaint": "medium",

            "other": "low"

        }

        context.severity = severity_map.get(
            context.case_type,
            "low"
        )

        return context
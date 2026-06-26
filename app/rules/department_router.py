from app.schemas.context import AnalysisContext


class DepartmentRouter:

    def process(self, context: AnalysisContext):

        if context.fraud:

            context.department = "fraud_investigation"

            return context

        mapping = {

            "wrong_transfer": "payments_operations",

            "payment_issue": "payments_operations",

            "double_charge": "billing",

            "complaint": "customer_support",

            "other": "customer_support"

        }

        context.department = mapping.get(
            context.case_type,
            "customer_support"
        )

        return context
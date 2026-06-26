from app.schemas.context import AnalysisContext

from app.ai.extractor import AIExtractor
from app.ai.generator import AIGenerator

from app.rules.transaction_matcher import TransactionMatcher
from app.rules.evidence_engine import EvidenceEngine
from app.rules.department_router import DepartmentRouter
from app.rules.severity_engine import SeverityEngine
from app.rules.review_engine import ReviewEngine
from app.rules.classifier import CaseClassifier


class InvestigationEngine:

    def __init__(self):

        self.extractor = AIExtractor()

        self.matcher = TransactionMatcher()

        self.evidence = EvidenceEngine()

        self.classifier = CaseClassifier()

        self.department = DepartmentRouter()

        self.severity = SeverityEngine()

        self.review = ReviewEngine()

        self.generator = AIGenerator()

    def run(
        self,
        context: AnalysisContext
    ) -> AnalysisContext:

        # --------------------------------
        # STEP 1
        # Gemini extracts information
        # --------------------------------

        extracted = self.extractor.process(
            context.complaint
        )

        context.intent = extracted.get(
            "intent",
            "other"
        )

        context.extracted_amount = extracted.get(
            "amount"
        )

        context.transaction_type = extracted.get(
            "transaction_type"
        )

        context.mentioned_time = extracted.get(
            "mentioned_time"
        )

        context.fraud = extracted.get(
            "fraud",
            False
        )

        context.confidence = extracted.get(
            "confidence",
            0.0
        )

        # --------------------------------
        # STEP 2
        # Investigation
        # --------------------------------

        context = self.matcher.process(context)

        context = self.evidence.process(context)

        context = self.classifier.process(context)

        context = self.department.process(context)

        context = self.severity.process(context)

        context = self.review.process(context)

        # --------------------------------
        # STEP 3
        # Generate responses
        # --------------------------------

        generated = self.generator.generate(

            complaint=context.complaint,

            case_type=context.case_type,

            evidence=context.evidence_verdict,

            department=context.department,

            severity=context.severity

        )

        context.agent_summary = generated.get(
            "agent_summary",
            ""
        )

        context.recommended_next_action = generated.get(
            "recommended_next_action",
            ""
        )

        context.customer_reply = generated.get(
            "customer_reply",
            ""
        )

        return context
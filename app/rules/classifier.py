from app.schemas.context import AnalysisContext


class CaseClassifier:

    def process(self, context: AnalysisContext):

        context.case_type = context.intent

        return context
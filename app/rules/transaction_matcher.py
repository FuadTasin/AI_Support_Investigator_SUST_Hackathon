from app.schemas.context import AnalysisContext


class TransactionMatcher:

    def process(self, context: AnalysisContext):

        best_transaction = None

        best_score = -1

        for txn in context.transaction_history:

            score = 0

            # -----------------------
            # Amount
            # -----------------------

            if (
                context.extracted_amount is not None
                and txn.amount == context.extracted_amount
            ):
                score += 60

            # -----------------------
            # Transaction Type
            # -----------------------

            if (
                context.transaction_type
                and txn.transaction_type.lower()
                == context.transaction_type.lower()
            ):
                score += 20

            # -----------------------
            # Status
            # -----------------------

            if txn.status.lower() == "completed":
                score += 10

            # -----------------------
            # Mentioned Time
            # -----------------------

            if context.mentioned_time:
                score += 10

            if score > best_score:

                best_score = score

                best_transaction = txn

        context.matched_transaction = best_transaction

        context.reason_codes.append(
            f"match_score={best_score}"
        )

        return context
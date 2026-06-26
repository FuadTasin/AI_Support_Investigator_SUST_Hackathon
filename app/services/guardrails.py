import re


class GuardRails:

    def __init__(self):

        self.blocked_patterns = [
            r"\botp\b",
            r"\bpin\b",
            r"\bpassword\b",
            r"share.*otp",
            r"share.*pin",
            r"share.*password",
            r"refund has been processed",
            r"money has been returned",
            r"guaranteed refund"
        ]

        self.replacements = {
            "refund has been processed":
                "If eligible, the refund will be processed through official channels.",

            "money has been returned":
                "If eligible, the amount will be returned after verification.",

            "guaranteed refund":
                "Refund eligibility will be determined after review."
        }

    def sanitize(self, text: str) -> str:

        if not text:
            return ""

        cleaned = text

        for bad, good in self.replacements.items():
            cleaned = re.sub(
                bad,
                good,
                cleaned,
                flags=re.IGNORECASE
            )

        return cleaned

    def contains_sensitive_request(self, text: str) -> bool:

        if not text:
            return False

        for pattern in self.blocked_patterns:

            if re.search(pattern, text, flags=re.IGNORECASE):
                return True

        return False
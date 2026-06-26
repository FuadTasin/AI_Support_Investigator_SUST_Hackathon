import json

from app.ai.prompts import GENERATION_PROMPT
from app.services.llm_service import LLMService
from app.services.guardrails import GuardRails


class AIGenerator:

    def __init__(self):

        self.llm = LLMService()

        self.guard = GuardRails()

    def generate(
        self,
        complaint,
        case_type,
        evidence,
        department,
        severity
    ):

        prompt = GENERATION_PROMPT.format(
            complaint=complaint,
            case_type=case_type,
            evidence=evidence,
            department=department,
            severity=severity
        )

        try:

            response = self.llm.generate(prompt)

            response = response.replace("```json", "")
            response = response.replace("```", "")

            data = json.loads(response)

        except Exception:

            data = {

                "agent_summary":
                    "Unable to generate AI summary.",

                "recommended_next_action":
                    "Escalate to human support.",

                "customer_reply":
                    "We have received your complaint and our team will review it shortly."

            }

        data["agent_summary"] = self.guard.sanitize(
            data.get("agent_summary", "")
        )

        data["recommended_next_action"] = self.guard.sanitize(
            data.get("recommended_next_action", "")
        )

        data["customer_reply"] = self.guard.sanitize(
            data.get("customer_reply", "")
        )

        return data
import json

from app.ai.prompts import EXTRACTION_PROMPT
from app.services.llm_service import LLMService


class AIExtractor:

    def __init__(self):
        self.llm = LLMService()

    def process(self, complaint: str):

        prompt = EXTRACTION_PROMPT.format(
            complaint=complaint
        )

        print("\n========== PROMPT ==========")
        print(prompt)

        response = self.llm.generate(prompt)

        print("\n========== RAW RESPONSE ==========")
        print(response)

        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        print("\n========== CLEANED RESPONSE ==========")
        print(response)

        data = json.loads(response)

        print("\n========== PARSED JSON ==========")
        print(data)

        return data
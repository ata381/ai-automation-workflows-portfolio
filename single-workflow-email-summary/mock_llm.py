class MockLLMClient:
    def summarise_email(self, email_text: str) -> dict:
        # Returns a realistic fake JSON-like dict: summary, urgency, suggested_action
        return {
            "summary": "Customer cannot access their account and has an urgent deadline.",
            "urgency": "high",
            "suggested_action": "Prioritise and resolve the login issue immediately."
        }

# To use a real LLM API (e.g. OpenAI), replace MockLLMClient with RealLLMClient and implement API calls.

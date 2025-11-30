class MockLLMClient:
    def summarise_email(self, email_text: str) -> dict:
        # Returns a realistic fake summary and sentiment
        return {
            "summary": "Customer requests a refund for a damaged item in order #12345.",
            "sentiment": "negative"
        }

    def extract_fields(self, email_text: str) -> dict:
        # Returns extracted fields from the sample email
        return {
            "name": "Jane Doe",
            "email": "jane.doe@email.com",
            "order_id": "12345",
            "topic": "refund",
            "sentiment": "negative"
        }

    def draft_reply(self, summary: dict, fields: dict) -> dict:
        # Returns a realistic draft reply
        return {
            "subject_line": f"Refund for Order #{fields['order_id']}",
            "body_text": f"Hi {fields['name']},\n\nWe’re sorry to hear about the damaged item. We’ve started processing your refund for order #{fields['order_id']}. You’ll receive confirmation soon.\n\nBest regards,\nSupport Team"
        }

# To use a real LLM API, replace MockLLMClient with RealLLMClient and implement API calls.

from mock_llm import MockLLMClient

SAMPLE_EMAIL = """Subject: Refund Request – Order #12345

Hi,

I received my order last week but one item was damaged. Can you please process a refund for order #12345? My email is jane.doe@email.com. I’m disappointed and hope this can be resolved quickly.

Thanks,
Jane Doe
"""

def main():
    print("Inbox Helper Workflow\n")
    email_text = SAMPLE_EMAIL

    llm = MockLLMClient()
    summary = llm.summarise_email(email_text)
    fields = llm.extract_fields(email_text)
    reply = llm.draft_reply(summary, fields)

    print("=== Summary ===")
    print("Summary:", summary["summary"])
    print("Sentiment:", summary["sentiment"])

    print("\n=== Extracted Fields ===")
    for k, v in fields.items():
        print(f"{k.capitalize()}: {v}")

    print("\n=== Draft Reply ===")
    print("Subject:", reply["subject_line"])
    print("Body:\n" + reply["body_text"])

    # To use a real LLM API, replace MockLLMClient with RealLLMClient and implement API calls.

if __name__ == "__main__":
    main()

from mock_llm import MockLLMClient

SAMPLE_EMAIL = """Subject: Account Access Issue

Hi team,

I’ve been trying to log into my account for the past two days but keep getting an error message. I need access urgently as I have a deadline tomorrow. Can you please help resolve this as soon as possible?

Thanks,
Alex
"""

def main():
    print("Email Summarisation Workflow\n")
    use_default = input("Use default sample email? (Y/n): ").strip().lower()
    if use_default in ('n', 'no'):
        print("Paste your email below. End with an empty line:")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        email_text = "\n".join(lines)
    else:
        email_text = SAMPLE_EMAIL

    llm = MockLLMClient()
    result = llm.summarise_email(email_text)

    print("\nSummary:", result["summary"])
    print("Urgency:", result["urgency"])
    print("Suggested action:", result["suggested_action"])

    # To use a real LLM API, replace MockLLMClient with RealLLMClient and implement API calls.

if __name__ == "__main__":
    main()

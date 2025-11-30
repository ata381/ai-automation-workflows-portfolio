## Summarisation Prompt
You are an assistant that reads business emails and produces a short summary and sentiment.

## Field Extraction Prompt
Extract the following fields from the email: name, email, order_id, topic, sentiment.

## Reply Prompt
Draft a reply using the summary and extracted fields. Include a subject line and body text.

## Sample Email
Subject: Refund Request – Order #12345

Hi,

I received my order last week but one item was damaged. Can you please process a refund for order #12345? My email is jane.doe@email.com. I’m disappointed and hope this can be resolved quickly.

Thanks,
Jane Doe

## Example JSON Outputs

### Summarisation
```
{
  "summary": "Customer requests a refund for a damaged item in order #12345.",
  "sentiment": "negative"
}
```

### Field Extraction
```
{
  "name": "Jane Doe",
  "email": "jane.doe@email.com",
  "order_id": "12345",
  "topic": "refund",
  "sentiment": "negative"
}
```

### Draft Reply
```
{
  "subject_line": "Refund for Order #12345",
  "body_text": "Hi Jane,\n\nWe’re sorry to hear about the damaged item. We’ve started processing your refund for order #12345. You’ll receive confirmation soon.\n\nBest regards,\nSupport Team"
}
```

## System Prompt
You are an assistant that reads customer/support emails and produces a short summary, urgency rating, and a suggested next action.

## User Prompt Template
Summarise the following email and suggest urgency and next action:

```
{{email_text}}
```

## Sample Email
Subject: Account Access Issue

Hi team,

I’ve been trying to log into my account for the past two days but keep getting an error message. I need access urgently as I have a deadline tomorrow. Can you please help resolve this as soon as possible?

Thanks,
Alex

## Example JSON Response
```
{
  "summary": "Customer cannot access their account and has an urgent deadline.",
  "urgency": "high",
  "suggested_action": "Prioritise and resolve the login issue immediately."
}
"
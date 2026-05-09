function AskFollowUpQuestion(asked_symptoms: string, conversation_history: string) -> string {
  client "CustomGemini"
  prompt #"
    You are an expert medical triage assistant. The user has mentioned some symptoms, but there is not enough context to proceed with a reliable medical search.

    Conversation History:
    {{ conversation_history }}

    Symptoms mentioned so far (Asked Symptoms):
    {{ asked_symptoms }}

    Based on the symptoms mentioned and the conversation history, generate a single, concise follow-up question to gather more specific details (such as duration, severity, exact location, or other accompanying symptoms).
    
    Return ONLY the question as plain text. Do not include quotes or any other formatting.
  "#
}

test sample_headache {
  functions [AskFollowUpQuestion]
  args {
    asked_symptoms #"headache"#
    conversation_history #"User: I have a headache."#
  }
}

test sample_fever {
  functions [AskFollowUpQuestion]
  args {
    asked_symptoms #"fever, coughing"#
    conversation_history #"User: My child has had a fever and keeps coughing."#
  }
}

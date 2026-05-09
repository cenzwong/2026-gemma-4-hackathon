class InformationEvaluation {
  has_enough_info bool @description("True if the user has provided sufficient medical details (symptoms, duration, context) to begin research, or false if more clarifying questions need to be asked.")
  confidence float @description("A value between 0.0 and 1.0 indicating how confident you are in this assessment.")
}

function EvaluateInformation(conversation: string) -> InformationEvaluation {
  client "CustomGemini"
  prompt #"
    You are an expert medical triage assistant. Your job is to determine if the user has provided enough information about their medical issue to proceed with detailed research and analysis.
    If the symptoms are too vague (e.g. "I have a headache"), you should return false. 
    If they provide detailed context (e.g. "I've had a severe throbbing headache on the right side of my head for 3 days with nausea"), return true.

    Evaluate the following conversation:
    {{ conversation }}

    {{ ctx.output_format }}
  "#
}

test sample_incomplete {
  functions [EvaluateInformation]
  args {
    conversation #"
      User: I have a headache.
    "#
  }
}

test sample_complete {
  functions [EvaluateInformation]
  args {
    conversation #"
      User: I've had a severe throbbing headache on the right side of my head for 3 days, accompanied by nausea and sensitivity to light.
    "#
  }
}

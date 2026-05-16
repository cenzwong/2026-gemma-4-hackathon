class ExtractedSymptoms {
  symptoms string[] @description("A list of symptoms or medical issues described by the user.")
}

function ExtractSymptoms(query: string) -> ExtractedSymptoms {
  client "CustomGemini"
  prompt #"
    You are an expert medical assistant. Extract a list of symptoms or medical issues mentioned in the user's query.
    If no symptoms are explicitly mentioned, return an empty list.

    User Query:
    {{ query }}

    {{ ctx.output_format }}
  "#
}

test sample_symptoms {
  functions [ExtractSymptoms]
  args {
    query #"
      Doctor, my chest feels like it's being crushed, and I'm sweating a bit.
    "#
  }
}

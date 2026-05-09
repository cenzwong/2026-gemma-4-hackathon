function DecodeQuestion(query: string) -> string[] {
  client "CustomGemini"
  prompt #"
    Given the following user medical query, extract the most important keywords or key phrases that would be useful for searching a medical database (like Wikipedia) to retrieve relevant articles for answering the query.
    Return a list of string query terms. Order them by importance.
    Limit to 3-5 key terms.

    User Query:
    {{ query }}

    {{ ctx.output_format }}
  "#
}

test sample_query {
  functions [DecodeQuestion]
  args {
    query #"
      What are the main symptoms of type 2 diabetes and how is it usually treated?
    "#
  }
}

from baml_client.sync_client import b
from baml_client.types import Resume

from dotenv import load_dotenv

load_dotenv()

def example(raw_resume: str) -> Resume: 
  # BAML's internal parser guarantees ExtractResume
  # to be always return a Resume type
  response = b.ExtractResume(raw_resume)
  return response

raw_resume = "Vaibhav Gupta<br>vbv@boundaryml.com<br><br>Experience:<br>- Founder at BoundaryML<br>- CV Engineer at Google<br>- CV Engineer at Microsoft<br><br>Skills:<br>- Rust<br>- C++"
resume = example(raw_resume)
print(resume.name)
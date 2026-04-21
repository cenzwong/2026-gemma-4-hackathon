from enum import Enum
from dataclasses import dataclass

@dataclass(frozen=True)
class ModelInfo:
    model_id: str
    architecture: str
    description: str

class GemmaModel(ModelInfo, Enum):
    GEMMA_4_26B_A4B_IT = (
        "gemma-4-26b-a4b-it",
        "Mixture-of-Experts (MoE)",
        "26 Billion total parameters with 4 Billion active parameters per token. It operates with a Standard context window. The primary goal is Throughput & Cost-Efficiency, suitable for High-volume APIs / Edge-ish deployments."
    )
    
    GEMMA_4_31B_IT = (
        "gemma-4-31b-it",
        "Dense",
        "31 Billion total parameters and 31 Billion active parameters per token. It has a 256,000 Tokens context window. The primary goal is Maximum Quality & Long-Context, ideal for Data Centers / Deep Research deployments."
    )

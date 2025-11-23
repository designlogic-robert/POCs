# tokens.py

from dataclasses import dataclass, field
import uuid
from datetime import datetime

@dataclass
class USToken:
    token_id: str
    domain: str          # e.g. "analysis", "finance", "narrative"
    intent: str          # high-level meaning
    payload: dict        # content / arguments
    created_at: str
    posture: str         # simplified version of Posture model

def build_example_token():
    """
    Example token representing:
    'Compare summaries of two docs and highlight risks.'
    """

    return USToken(
        token_id=str(uuid.uuid4()),
        domain="analysis",
        intent="compare_documents",
        payload={
            "doc_a": "Summary of document A...",
            "doc_b": "Summary of document B..."
        },
        created_at=datetime.utcnow().isoformat(),
        posture="analytic"
    )


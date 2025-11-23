# scp_layer.py

from dataclasses import dataclass

@dataclass
class SCPDirective:
    directive: str      # e.g. "DOC_COMPARE"
    plan_template: str  # ORCH-C plan ID
    metadata: dict

def scp_classify(token):
    """
    Classify the USToken into a semantic directive.
    In real SCP this would read token families, invariants, posture, etc.
    """

    if token.intent == "compare_documents":
        return SCPDirective(
            directive="DOC_COMPARE",
            plan_template="PLAN_COMPARE_V1",
            metadata={"confidence": 0.92}
        )

    # fallback — deterministic
    return SCPDirective(
        directive="UNKNOWN",
        plan_template="PLAN_FALLBACK",
        metadata={"confidence": 0.55}
    )


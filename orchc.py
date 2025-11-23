# orchc.py

from dataclasses import dataclass

@dataclass
class ExecutionStep:
    step: str
    args: dict

@dataclass
class ExecutionPlan:
    plan_id: str
    steps: list

def orchc_build_plan(scp_directive, token):
    """
    Deterministically convert an SCP directive into an ExecutionPlan.
    """

    if scp_directive.plan_template == "PLAN_COMPARE_V1":
        steps = [
            ExecutionStep(
                step="extract_features",
                args={"text_a": token.payload["doc_a"],
                      "text_b": token.payload["doc_b"]}
            ),
            ExecutionStep(
                step="compare",
                args={}
            ),
            ExecutionStep(
                step="summarize_risks",
                args={}
            )
        ]

        return ExecutionPlan(
            plan_id="COMPARE_EXECUTION",
            steps=steps
        )

    # fallback deterministic
    return ExecutionPlan(
        plan_id="FALLBACK_EXECUTION",
        steps=[ExecutionStep(step="echo", args={"msg": "fallback"})]
    )

def orchc_execute(plan, llm_client):
    """
    Execute a deterministic step-by-step plan.
    llm_client is a stub.
    """

    logs = []

    for step in plan.steps:
        result = llm_client(step.step, step.args)
        logs.append((step.step, result))

    return {
        "plan_id": plan.plan_id,
        "log": logs
    }


# main.py

from tokens import build_example_token
from scp_layer import scp_classify
from orchc import orchc_build_plan, orchc_execute

# -------------------------------
# Dummy LLM client (deterministic)
# -------------------------------

def dummy_llm_client(step_name, args):
    if step_name == "extract_features":
        return {
            "features_a": ["risk_A1", "topic_A2"],
            "features_b": ["risk_B1", "topic_B2"]
        }

    if step_name == "compare":
        return {
            "overlap": ["topic_A2"],
            "differences": ["risk_A1", "risk_B1"]
        }

    if step_name == "summarize_risks":
        return {
            "risk_summary": "Document A has risk_A1; Document B has risk_B1."
        }

    return {"result": "noop"}

# -------------------------------
# POC Pipeline
# -------------------------------

if __name__ == "__main__":
    # 1. Token birth
    token = build_example_token()

    # 2. SCP classification
    directive = scp_classify(token)

    # 3. Build execution plan
    plan = orchc_build_plan(directive, token)

    # 4. Execute plan deterministically
    output = orchc_execute(plan, dummy_llm_client)

    # Show output
    print("\n=== SYNCE POC OUTPUT ===")
    print("Token:", token)
    print("Directive:", directive)
    print("Execution Plan:", plan)
    print("\nExecution Log:")
    for step, result in output["log"]:
        print(f"- {step}: {result}")


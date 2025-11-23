# SynCE POC – UST + SCP + ORCH-C (Python)

This is a small proof-of-concept that demonstrates the core semantic cycle of the SynCE architecture:

> UST Token → SCP Directive → ORCH-C Execution Plan → Deterministic Execution → Log

The goal is not to show UI or infrastructure, but to prove that:

- A **universal semantic token** (UST) can encode intent and payload.
- A **Semantic Control Protocol** (SCP) can classify intent and choose a plan template.
- A **deterministic orchestrator** (ORCH-C-like core) can turn that into a concrete step-by-step ExecutionPlan.
- The plan can be executed against a language model client in a fully traceable way.

In this POC, the language model client is a **dummy stub** so the demo is fully offline and reproducible.  
You can later replace the stub with a real OpenAI client.

---

## How it works

The POC runs through the following stages:

1. **UST Token birth**

   `build_example_token()` creates a semantic token representing:

   > “Compare summaries of two docs and highlight risks.”

   The token has:
   - `family="SemanticToken"`
   - a high-level `intent`
   - a `payload` containing two example documents
   - a `posture` (Cognitive)

2. **UST validation**

   `validate_token(token)` enforces minimal invariants:
   - token has an id, family, intent
   - payload is a dict
   - posture is one of {Cognitive, Affective, Ethical, Pragmatic}

3. **SCP classification**

   `run_scp(token)`:

   - classifies the intent into an `intent_class`  
   - selects a `plan_template` for ORCH-C  
   - wraps both in a `ControlDirective`

4. **ORCH-C plan construction**

   `build_plan_from_directive(directive)` builds an `ExecutionPlan`:

   For the default example, the plan has three steps:

   1. summarize documents
   2. analyze risks/uncertainties
   3. format the final answer

5. **Plan execution**

   `execute_plan(plan, llm, initial_ctx)` runs each step, logs:

   - step index
   - name
   - description
   - marker
   - duration

   The final context contains a `final_answer` field.

6. **Output**

   `main.py` prints:

   - token creation info
   - SCP classification
   - ORCH-C plan overview
   - final answer (from DummyLLM)
   - JSON execution log

---

## Running the POC

Requirements:

- Python 3.9 or newer
- No external dependencies required

Steps:

```bash
cd synce_poc
python main.py

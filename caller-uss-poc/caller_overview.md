# CALLER on top of USS

CALLER is the human-facing layer that sits above the Universal Semantic Stack (USS).  
Its role is simple: take a human request, interpret it semantically, route it through the USS runtime, and return a structured, actionable answer.

CALLER does **not** replace USS.  
CALLER is the *interface* that lets humans use it.

## How the layers fit together

- **USS / UST**  
  Provides the meaning substrate and token model.

- **USR**  
  The deterministic runtime and planner that turns intent into a small, auditable execution plan.

- **SCP**  
  The directive and routing protocol that connects CALLER to the engines.

- **Engines**  
  Narrow, deterministic domain functions (or tools, or prompts) that do real work.

- **CALLER**  
  Wraps everything into one API surface a human can actually talk to.

In other words:

> Humans talk to CALLER.  
> CALLER talks to USS.  
> USS does the thinking.

## What this POC demonstrates

The POC chooses a small domain — support inbox triage — and shows how CALLER uses the USS pattern to:

1. Interpret intent from a noisy human request.  
2. Ask USR to build a deterministic plan.  
3. Call domain engines in the correct order.  
4. Assemble a structured human-readable output.

This is the same pattern you would use in any vertical:

- Construction intelligence (Apex)  
- Finance intelligence  
- Operations triage  
- Code review  
- Data room analysis  
- Anything requiring structured reasoning

CALLER is the “professional assistant” personality on top of USS.  
You can swap domains without rewriting the architecture.

## Why this matters for founders or technical leads

- It shows structured reasoning rather than LLM improvisation.
- It demonstrates deterministic planning instead of hidden chain-of-thought.
- It presents clean separation of layers: interface, planner, engines.
- It shows how USS prevents hallucination drift by forcing every step to be explicit.

This POC is intentionally tiny, but the pattern scales into full products.
Reading this overview gives founders and technical leads a clear, approachable
understanding of why USS matters and how CALLER serves as the interface layer
for real-world systems.


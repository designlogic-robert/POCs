# CALLER + USS POC

This folder contains a small proof of concept that shows how CALLER sits on top of the USS stack:

- CALLER = human interface and orchestrator
- USR = planning layer that turns intent into a small execution plan
- Engines = simple domain engines that do narrow tasks
- Output = a structured summary that a founder or lead can act on

The scenario: CALLER receives a snapshot of a SaaS support inbox and has to:

1. Detect the main user pain patterns
2. Decide what to fix first
3. Suggest how to route work internally

## Files

- `caller_overview.md`  
  Conceptual overview of CALLER and how it relates to USS.

- `caller_walkthrough.md`  
  Step-by-step explanation of what the POC does and how it maps to the architecture.

- `caller_poc.py`  
  Executable Python script that simulates CALLER + USR + engines.  
  It prints both the internal steps (debug view) and the final human report.

## How to run

From a terminal or PowerShell:

```bash
cd path\to\caller-uss-poc
python caller_poc.py
```

# You should see:

A series of ### STEP N blocks that show the internal pipeline.

A final markdown style report that looks like a triage summary for a support lead.

This is not production code. It is a narrative POC that lets founders and engineers feel the USS orchestration pattern in a very small, inspectable file.


---


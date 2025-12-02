# USS Proof-of-Concepts (POCs)

This repository contains small, focused Proof-of-Concept implementations demonstrating key ideas from the **Universal Semantic Systems (USS)** architecture.  
Each POC is self-contained, easy to run, and illustrates how USS enables structured reasoning, deterministic planning, and semantic control on top of foundation models.

---

## 📁 Included POCs

### 1. `caller-uss-poc/`
A minimal, executable demonstration of **CALLER**, the USS request-orchestration layer.

This POC shows:
- How a request enters the system through a structured message schema  
- How CALLER interprets intent and extracts required tasks  
- How USR (Universal Semantic Runtime) creates a deterministic plan  
- How small “engines” produce structured, auditable outputs  
- How CALLER assembles everything into a clean, final answer  

**Why this matters:**  
It demonstrates the USS pattern: structured reasoning → controlled planning → reproducible, non-hallucinatory outputs.

**Files:**
- `caller_poc.py` — fully executable Python POC  
- `caller_overview.md` — concept and architecture explanation  
- `caller_walkthrough.md` — step-by-step example flow  
- `README.md` — usage instructions  

Run with:
```bash
python caller_poc.py
```
### 2. `synce-poc/`
This POC demonstrates a **minimal, self-contained simulation** of the core USS execution pattern using SynCE-style components.  
It is not a full runtime — it’s a compact, readable demo showing how semantic tokens, SCP routing, deterministic planning, and engine execution interact.

Perfect for founders, recruiters, or collaborators who want to *see* how USS behaves in code.

---

# What This POC Shows

### ✅ Semantic Tokens  
How raw input becomes **structured semantic units** (`tokens.py`).

### ✅ SCP (Semantic Control Protocol) Routing  
How SCP interprets tokens and selects appropriate actions (`scp_layer.py`).

### ✅ Deterministic Planning (ORCH-C Mini)  
A tiny version of ORCH-C that turns intent into a **linear, explicit execution plan** (`orchc.py`).

### ✅ Engine Execution  
`main.py` runs the full cycle:
1. Ingest raw input  
2. Tokenize  
3. SCP routing  
4. ORCH-C planning  
5. Engine execution  
6. Output assembly  

### ✅ Example Output  
`example_output.txt` shows what a complete run looks like.

This demonstrates **the signature properties of USS**:
- No chain-of-thought improvisation  
- Explicit intermediate states  
- Deterministic reasoning path  
- Clear separation of layers  

---

# File Overview
```
synce-poc/
│
├── docs/ # (Optional) project notes / architecture diagrams
│
├── main.py # Entry point – runs the full POC
├── tokens.py # Semantic token definitions
├── scp_layer.py # Semantic Control Protocol logic
├── orchc.py # Deterministic planner (mini ORCH-C)
├── example_output.txt # Sample output from a full run
├── requirements.txt # Dependencies (very lightweight)
│
├── LICENSE # Apache 2.0 (open + safe to use)
└── README.md # This file
```
---

# Running the POC

### 1. Install dependencies
```bash
pip install -r requirements.txt
```
2. Run the demo
```bash
python main.py
```
You’ll see a full USS-style reasoning flow printed to the console.

### Why This Matters

- This POC is intentionally tiny, but it demonstrates:
- How USS structures meaning before reasoning
- How semantic tokens drive deterministic planning
- How SCP + ORCH-C remove hallucination drift
- How the system remains fully inspectable, step-by-step

Anyone reviewing this POC gets a clear sense of what makes USS different from “just another LLM wrapper.”

## 🌐 Purpose of This Repository

### These POCs help:
- founders
- technical leads
- recruiters
- collaborators
- platform architects

…quickly understand the practical value of USS through compact, observable examples.

They are not production code.
They are clarity tools showcasing how USS behaves in small, testable environments.

## 🧱 What USS Demonstrates Across These POCs

- Deterministic orchestration above any LLM
- Layered semantic architecture (Tokens → SCP → USR → Engines)
- Explicit, machine-auditable reasoning
- No improvisational chain-of-thought
- Stable, reproducible outputs
- A universal pattern for multi-domain reasoning systems

### 📬 Contact
Robert Hansen
Chief Semantic Architect — USS
- GitHub: https://github.com/designlogic-robert
- LinkedIn: https://www.linkedin.com/in/roberthansen-ai

### 🔑 License
All POCs in this repository are released under Apache 2.0 unless otherwise noted.


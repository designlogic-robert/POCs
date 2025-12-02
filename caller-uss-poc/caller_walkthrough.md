# CALLER POC walkthrough

This is what happens when you run `python caller_poc.py`.

## Step 1: CALLER receives a message

We build a simple message object with:

- Who is asking (role, company)
- Their goal (stabilize product, reduce churn)
- A synthetic snapshot of support tickets

This stands in for the "message schema" you would send from a UI, Slack bot, or API.

## Step 2: CALLER interprets intent

CALLER reads the message and decides:

- Primary intent: "Triage incoming support issues"
- Time horizon: "Fix the worst problems in the next few days"
- Focus: "Revenue and trust risk, not cosmetic annoyances"

In a real system this is where semantic tokens and posture live.  
In the POC we show it as a small intent dictionary.

## Step 3: USR builds a plan

CALLER hands the interpreted intent to USR.

USR returns a very small plan, for example:

1. Summarize the main user pain patterns
2. Rank what to fix first
3. Suggest internal routing by team

This is the same shape you would use for more complex multi step plans.

## Step 4: Engines run

For each step, CALLER calls a tiny "engine" function:

- `summarize_patterns` looks at the tickets and groups them
- `recommend_fixes` decides what to fix first
- `suggest_routing` maps issues to internal teams

In a real USS deployment these engines could be LLM prompts, tools, or services.  
Here they are simple deterministic Python functions.

## Step 5: CALLER assembles the answer

Finally CALLER takes:

- The interpreted intent
- The engine outputs

and assembles a markdown style report for the human, which you see at the bottom of the script output.

The important part is the *shape* of the flow, not the specific domain.  
You can swap the support tickets for construction documents, financial data, or anything else, and the pattern still holds.

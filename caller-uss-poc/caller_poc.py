"""
CALLER + USS POC

Single file demo that shows:
- Message schema
- Intent interpretation
- USR-style planning
- Engine calls
- Final human-facing report
"""

DEBUG = True  # set to False if you only want the final report


# ---------- 1. Message building ----------

def build_message():
    """Simulate a request coming from a support lead."""
    return {
        "company": "Acme SaaS",
        "role": "Head of Product",
        "goal": "Understand what is hurting users most and what to fix first.",
        "inbox_snapshot": [
            {
                "id": 1,
                "text": "I was charged twice this month again. If this happens one more time I am cancelling.",
            },
            {
                "id": 2,
                "text": "After I reset my password the app keeps logging me out and I cannot stay signed in.",
            },
            {
                "id": 3,
                "text": "The app is so slow every evening around 7pm that my team just gives up.",
            },
            {
                "id": 4,
                "text": "The dark mode toggle disappeared. Annoying, but I can live with it for now.",
            },
        ],
    }


# ---------- 2. Intent interpretation (CALLER) ----------

def interpret_intent(message):
    """Turn the raw message into a simple intent object."""
    return {
        "primary_task": "support_triage",
        "time_horizon": "this_week",
        "risk_focus": "revenue_and_trust",
        "role": message["role"],
        "company": message["company"],
        "summary": (
            "Triage support inbox, detect main patterns, "
            "prioritize fixes, and suggest routing by team."
        ),
    }


# ---------- 3. Planning (USR) ----------

def plan_with_usr(intent):
    """Return a small deterministic execution plan."""
    return [
        {
            "step": 1,
            "name": "summarize_patterns",
            "description": "Group tickets into main user pain patterns.",
        },
        {
            "step": 2,
            "name": "recommend_fixes",
            "description": "Rank which patterns to fix first.",
        },
        {
            "step": 3,
            "name": "suggest_routing",
            "description": "Suggest which teams should own each pattern.",
        },
    ]


# ---------- 4. Engines ----------

def summarize_patterns(tickets):
    patterns = []

    patterns.append({
        "label": "Billing double charges",
        "impact": "High",
        "urgency": "High",
        "tickets": [t for t in tickets if "charged twice" in t["text"] or "charged" in t["text"]],
        "notes": "Revenue and trust risk. Users explicitly threaten to churn.",
    })

    patterns.append({
        "label": "Login after password reset",
        "impact": "High",
        "urgency": "Medium",
        "tickets": [t for t in tickets if "reset my password" in t["text"] or "logging me out" in t["text"]],
        "notes": "Blocks access, but fewer churn threats than billing.",
    })

    patterns.append({
        "label": "Slow app during peak hours",
        "impact": "Medium",
        "urgency": "Medium",
        "tickets": [t for t in tickets if "slow every evening" in t["text"]],
        "notes": "Annoying but less catastrophic than billing or login issues.",
    })

    patterns.append({
        "label": "UX annoyances",
        "impact": "Low",
        "urgency": "Low",
        "tickets": [t for t in tickets if "dark mode" in t["text"]],
        "notes": "Do not schedule before core reliability work.",
    })

    return patterns


def recommend_fixes(patterns):
    """Simple ranking rule: High > Medium > Low, tie break by churn risk."""
    impact_order = {"High": 3, "Medium": 2, "Low": 1}

    scored = []
    for p in patterns:
        score = impact_order.get(p["impact"], 0)
        if "churn" in p["notes"].lower():
            score += 1
        scored.append((score, p))

    scored.sort(reverse=True, key=lambda x: x[0])
    ordered = [p for _, p in scored]

    recommendations = []
    for idx, p in enumerate(ordered, start=1):
        if "Billing" in p["label"]:
            action = "Hotfix billing double charge bug and add automated detection to reverse duplicates."
        elif "Login" in p["label"]:
            action = "Stabilize login flow after password reset and add monitoring."
        elif "Slow app" in p["label"]:
            action = "Improve performance profiling and simple throttling during peak hours."
        else:
            action = "Schedule UX cleanups after reliability work is stable."

        recommendations.append({
            "rank": idx,
            "pattern": p["label"],
            "recommended_action": action,
        })

    return recommendations


def suggest_routing(patterns):
    routing = []
    for p in patterns:
        if "Billing" in p["label"]:
            team = "Payments team"
            target = "Fix within 48 hours."
        elif "Login" in p["label"]:
            team = "Auth team"
            target = "Fix within 5 days."
        elif "Slow app" in p["label"]:
            team = "Platform team"
            target = "Start investigation this week."
        else:
            team = "Product design"
            target = "Bundle into next minor release."

        routing.append({
            "pattern": p["label"],
            "team": team,
            "target": target,
        })

    return routing


# ---------- 5. Assembly (CALLER) ----------

def render_markdown_summary(intent, patterns, fixes, routing):
    lines = []

    lines.append("Here is what I am seeing from a synthetic snapshot of your support inbox.\n")
    lines.append("## 1. The main patterns\n")

    for idx, p in enumerate(patterns, start=1):
        lines.append(f"{idx}. **{p['label']}**")
        lines.append(f"   - Impact: {p['impact']}, urgency: {p['urgency']}.")
        lines.append(f"   - Notes: {p['notes']}\n")

    lines.append("## 2. What to fix first\n")

    for r in fixes:
        lines.append(f"{r['rank']}. **{r['pattern']}**")
        lines.append(f"   - {r['recommended_action']}\n")

    lines.append("## 3. Suggested internal routing\n")

    for r in routing:
        lines.append(f"- **{r['team']}** → Own {r['pattern']}. Target: {r['target']}")

    return "\n".join(lines)


# ---------- 6. Main orchestration ----------

def main():
    message = build_message()
    if DEBUG:
        print("### STEP 1: Raw request message\n")
        print(message, "\n")

    intent = interpret_intent(message)
    if DEBUG:
        print("### STEP 2: Interpreted intent\n")
        print(intent, "\n")

    plan = plan_with_usr(intent)
    if DEBUG:
        print("### STEP 3: USR plan\n")
        for step in plan:
            print(step)
        print()

    tickets = message["inbox_snapshot"]
    patterns = summarize_patterns(tickets)
    fixes = recommend_fixes(patterns)
    routing = suggest_routing(patterns)

    if DEBUG:
        print("### STEP 4: Engine outputs\n")
        print("Patterns:")
        for p in patterns:
            print(" ", p)
        print("\nFix recommendations:")
        for f in fixes:
            print(" ", f)
        print("\nRouting suggestions:")
        for r in routing:
            print(" ", r)
        print("\n")

    summary = render_markdown_summary(intent, patterns, fixes, routing)

    print(summary)


if __name__ == "__main__":
    main()

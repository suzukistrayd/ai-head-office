---
type: workflow
name: triggers
version: 1.0
---

# STRAYD — Automation Triggers

## Trigger Types

### 1. Scheduled (Automatic)

Daily 6pm (X, IG, TikTok drafts)
Monday 9am (Weekly content plan)
Sunday 8am (Research agent)


### 2. Event-Based (Automatic)
GitHub push → Sync knowledge
New file in INPUT → Intake agent
Issue created → Research agent


### 3. Manual (On-Demand)
workflow_dispatch button
Dashboard [RUN] buttons
Obsidian command


### 4. Hybrid (All Active)
All three trigger types run simultaneously.

---

## GitHub Actions Triggers

| Workflow | Trigger |
|----------|---------|
| daily-social.yml | schedule + workflow_dispatch |
| weekly-content.yml | schedule + workflow_dispatch |
| research-agent.yml | schedule + workflow_dispatch |
| approve-post.yml | workflow_dispatch |

---

## Dashboard Quick Actions

| Button | Action |
|--------|---------|
| 📝 Write Post | Generate X post |
| 🎨 Gen Image | Run Colab workflow |
| 📂 Sort Data | Run intake agent |
| 📊 View Posts | Open content/approved |
| 🔄 Sync | GitHub sync |

---

## Status Indicators

| Status | Meaning |
|--------|---------|
| 🟢 LIVE | Working, last run success |
| 🟡 PENDING | In queue or scheduled |
| 🔴 ERROR | Failed, needs attention |
| ⬜ READY | Awaiting trigger |

---

© 2026 SS SUZUKI & STRAYD

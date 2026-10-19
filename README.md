# Automation Rescue — verified workflow proofs

Small public proof-of-work repository for automation/integration work.

This is **not client code**. It contains synthetic demos that exercise patterns I use when building reliable workflow systems:

1. **Lead routing** — validates/normalizes input and deterministically chooses a priority/next action.
2. **Idempotency / duplicate protection** — the same event ID is processed once and subsequent replays are ignored.
3. **Human approval gate** — only high-confidence, low-risk actions auto-execute; uncertain/risky cases require human review.

## Live proof

- [42-second sandbox screencast (synthetic data)](assets/NeuroCore_Sandbox_LiveProof_20261019.mp4) — demonstrates lead routing, duplicate suppression and human-review gating. Recorded 2026-10-19 from an isolated localhost test; **not a live client integration**.

The previous ephemeral Cloudflare preview URL has expired (DNS unavailable when checked 2026-10-19). Use the recording above for a quick walkthrough or run the open-source demos locally using the steps below. **There is currently no public live server or customer deployment.**

## Paid fixed-scope pilot

**Automation Rescue QA — fixed PLN 790 (or USD 199), subject to a written scope.**
For an agency or company with one already-existing n8n/Make/Python workflow
that fails, duplicates events, or needs a human approval gate.

- **Inputs:** a sanitized workflow export, sample test events and one written acceptance criterion.
- **Deliverables:** reproducible diagnosis, failure evidence, minimal patch or clearly documented blocker, and a short validation report.
- **Limit:** one workflow / one issue class / maximum two hours of investigation, plus one clarification round.
- **Payment:** buyer-funded fixed milestone via [Useme](https://useme.com/) before work begins; no free implementation or unsolicited access.
- **Safety:** no client passwords, access tokens, live database dumps, unauthorized API calls or production deployment without permission.
- **Proof:** the synthetic video above and the reproducible local tests. These are not testimonials or a production client case study.

**Request a paid pilot:** [Email NeuroCore business](mailto:system.mozg.office@gmail.com?subject=Automation%20Rescue%20-%20paid%20pilot).
Send a non-sensitive failure description and the intended acceptance criterion.
We'll confirm scope, capacity and the exact Useme invoice amount before any client work.

## Run locally

    python3 demo_server.py
    python3 smoke_test.py

The server listens on 127.0.0.1:8089 by default.

## Scope

The code intentionally stays small and inspectable. The point is to demonstrate the control patterns, not to pretend this is a full CRM or production SaaS.

Typical paid work: n8n/Make-style orchestration, APIs/webhooks, Python glue code, Gmail/Google integrations, retries, deduplication, logging and human approval gates.

Contact: system.mozg.office@gmail.com

# Automation Rescue — verified workflow proofs

Small public proof-of-work repository for automation/integration work.

This is **not client code**. It contains synthetic demos that exercise patterns I use when building reliable workflow systems:

1. **Lead routing** — validates/normalizes input and deterministically chooses a priority/next action.
2. **Idempotency / duplicate protection** — the same event ID is processed once and subsequent replays are ignored.
3. **Human approval gate** — only high-confidence, low-risk actions auto-execute; uncertain/risky cases require human review.

## Live proof

- [42-second sandbox screencast (synthetic data)](assets/NeuroCore_Sandbox_LiveProof_20261019.mp4) — demonstrates lead routing, duplicate suppression and human-review gating. Recorded 2026-10-19 from an isolated localhost test; **not a live client integration**.

The previous ephemeral Cloudflare preview URL has expired (DNS unavailable when checked 2026-10-19). Use the recording above for a quick walkthrough or run the open-source demos locally using the steps below. **There is currently no public live server or customer deployment.**

## Run locally

    python3 demo_server.py
    python3 smoke_test.py

The server listens on 127.0.0.1:8089 by default.

## Scope

The code intentionally stays small and inspectable. The point is to demonstrate the control patterns, not to pretend this is a full CRM or production SaaS.

Typical paid work: n8n/Make-style orchestration, APIs/webhooks, Python glue code, Gmail/Google integrations, retries, deduplication, logging and human approval gates.

Contact: system.mozg.office@gmail.com

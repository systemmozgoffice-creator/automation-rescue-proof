# Automation Rescue — verified workflow proofs

Small public proof-of-work repository for automation/integration work.

This is **not client code**. It contains synthetic demos that exercise patterns I use when building reliable workflow systems:

1. **Lead routing** — validates/normalizes input and deterministically chooses a priority/next action.
2. **Idempotency / duplicate protection** — the same event ID is processed once and subsequent replays are ignored.
3. **Human approval gate** — only high-confidence, low-risk actions auto-execute; uncertain/risky cases require human review.

## Live proof

- Landing page: https://contributed-dinner-transaction-cement.trycloudflare.com/
- Interactive demos: https://contributed-dinner-transaction-cement.trycloudflare.com/proof
- Health: https://contributed-dinner-transaction-cement.trycloudflare.com/api/health
- Evidence counters: https://contributed-dinner-transaction-cement.trycloudflare.com/api/demo/evidence

The live URL is a temporary Cloudflare tunnel, so the repository remains the durable reference.

## Run locally

    python3 demo_server.py
    python3 smoke_test.py

The server listens on 127.0.0.1:8089 by default.

## Scope

The code intentionally stays small and inspectable. The point is to demonstrate the control patterns, not to pretend this is a full CRM or production SaaS.

Typical paid work: n8n/Make-style orchestration, APIs/webhooks, Python glue code, Gmail/Google integrations, retries, deduplication, logging and human approval gates.

Contact: system.mozg.office@gmail.com

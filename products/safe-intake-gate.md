# NeuroCore Safe Intake Gate — n8n Starter Kit v1

**A small, inspectable fail-closed decision gate for n8n builders.**  
**Status: PREVIEW / WAITLIST — checkout is not live yet. Do not send payments.**

## The problem

A workflow that accepts incoming events may accidentally continue processing when
consent is missing, personally identifiable information has not been cleared, or
an external publication is requested. This starter kit shows a conservative
*review-only* decision step that refuses those cases.

## What is included

- One **inactive, importable** n8n example (Manual Trigger -> Synthetic intake -> Client safety gate).
- Five synthetic test cases with explicit expected results.
- A Node.js offline test harness (11 checks) that runs the actual supplied Code node logic.
- Setup instructions, SHA-256 file manifest and a non-exclusive buyer-use license.
- A single ZIP download **when checkout is activated**; no subscription or API keys needed.

## Verified test matrix

| Synthetic case | Expected decision |
| --- | --- |
| Internal review, cleared synthetic input | GO_REVIEW_ONLY |
| Consent missing | HOLD_CONSENT |
| PII not cleared | HOLD_PII |
| External destination requested | HOLD_DESTINATION |
| Unsupported schema | HOLD_SCHEMA |

Every output sets **publish_allowed=false** and **external_calls=0**.

**Evidence:** The five decision cases and additional safety checks passed on
Node.js v22 using the exact n8n Code node JavaScript in an isolated test.
The ZIP passes archive-integrity verification.

**Additional real n8n run (2026-10-20):** the exact offline workflow was
imported into a disposable n8n Docker instance, with outbound networking
disabled, no customer data and no exposed service ports. The CLI reported
`Successfully imported 1 workflow`, `status: success`,
`finished: true` and completion of the `Client safety gate` Code node.
All five case identifiers and their decisions were visible in the execution
trace. Strict independent machine comparison of all output fields against
the expected JSON has **not** been completed. There was no real third-party
API integration, live consent/PII verification or customer publication.
This template is not marketed as production-certified.

## Intended user

n8n/automation builders who want a minimal example of review-only gating
and automated regression checks. This is a starting pattern to adapt,
not a production consent-management or PII-detection service.

## Limitations

- No OAuth, external CRM, WhatsApp, TikTok, YouTube or automatic publishing.
- Consent and PII flags are **provided by the sample input**. They are *not*
  independently verified or detected.
- GO_REVIEW_ONLY is permission for an operator to review, **not** publish.
- No persistent deduplication, security certification, or legal-compliance guarantee.
- No included hosting, installation or maintenance.

## Price and availability

**Proposed introductory price: USD $9** for the download. Final price,
taxes, currency and payment method are subject to a working seller checkout
and may change. **There is no active purchase link or payment collection.**

Would this narrowly scoped, testable starter kit be useful for your work?
[Email NeuroCore to request launch notification](mailto:system.mozg.office@gmail.com?subject=NeuroCore%20Safe%20Intake%20Gate%20-%20launch%20notification).
Please do not send credentials or real customer data.

*Last verified 2026-10-20. Created from a generic internal NeuroCore sample,
not from any customer's paid deliverables.*

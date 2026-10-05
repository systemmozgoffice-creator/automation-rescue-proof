import json, subprocess, time, urllib.request, uuid

BASE = "http://127.0.0.1:8089"

def call(path, payload=None):
    data = None if payload is None else json.dumps(payload).encode()
    req = urllib.request.Request(BASE + path, data=data,
        headers={"Content-Type":"application/json"} if data else {})
    with urllib.request.urlopen(req, timeout=3) as r:
        return r.status, json.loads(r.read())

p = subprocess.Popen(["python3", "demo_server.py"])
try:
    time.sleep(.5)
    assert call("/api/health")[1]["status"] == "ok"

    lead = call("/api/demo/lead", {
        "email":"buyer@example.com", "source":"website",
        "message":"Need urgent API integration quote today"
    })[1]
    assert lead["priority"] == "high"
    assert lead["next_action"] == "sales_review_now"

    eid = "test-" + str(uuid.uuid4())
    assert call("/api/demo/idempotency", {"event_id":eid})[1]["status"] == "processed"
    assert call("/api/demo/idempotency", {"event_id":eid})[1]["status"] == "duplicate_ignored"

    assert call("/api/demo/gate", {"confidence":.91,"risk":"low"})[1]["decision"] == "auto_execute"
    assert call("/api/demo/gate", {"confidence":.72,"risk":"medium"})[1]["decision"] == "human_review"

    print("PASS: 6 assertions across health, routing, idempotency and human gate")
finally:
    p.terminate()
    p.wait(timeout=3)

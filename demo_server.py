from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import datetime, json, sqlite3, threading, uuid

DB = "/tmp/automation_rescue_demo.db"
LOCK = threading.RLock()

def now():
    return datetime.datetime.now(datetime.UTC).replace(microsecond=0).isoformat()

def init_db():
    with sqlite3.connect(DB) as con:
        con.execute("create table if not exists idem (event_id text primary key, ts text not null)")

class H(BaseHTTPRequestHandler):
    def log_message(self, *_): pass

    def json(self, code, obj):
        body = json.dumps(obj, indent=2).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def read_json(self):
        n = int(self.headers.get("Content-Length", "0"))
        if n <= 0 or n > 10_000:
            raise ValueError("invalid_body_size")
        return json.loads(self.rfile.read(n))

    def do_GET(self):
        if self.path == "/api/health":
            return self.json(200, {"status": "ok", "utc": now()})
        return self.json(404, {"status": "not_found"})

    def do_POST(self):
        try:
            data = self.read_json()
        except Exception as exc:
            return self.json(400, {"status": "error", "error": str(exc)})

        if self.path == "/api/demo/lead":
            email = str(data.get("email", "")).strip().lower()
            source = str(data.get("source", "unknown")).strip()
            message = str(data.get("message", "")).strip()
            if "@" not in email or not message:
                return self.json(400, {"status": "error", "error": "valid email and message required"})
            urgent = any(x in (message + " " + source).lower()
                         for x in ("urgent", "today", "asap", "broken", "failing", "quote"))
            priority = "high" if urgent else "normal"
            return self.json(200, {
                "status": "processed",
                "proof_id": str(uuid.uuid4()),
                "normalized": {"email": email, "source": source},
                "priority": priority,
                "next_action": "sales_review_now" if urgent else "sales_queue",
            })

        if self.path == "/api/demo/idempotency":
            event_id = str(data.get("event_id", "")).strip()
            if not event_id:
                return self.json(400, {"status": "error", "error": "event_id required"})
            with LOCK, sqlite3.connect(DB) as con:
                try:
                    con.execute("insert into idem(event_id,ts) values(?,?)", (event_id, now()))
                    con.commit()
                    status = "processed"
                except sqlite3.IntegrityError:
                    con.rollback()
                    status = "duplicate_ignored"
            return self.json(200, {"status": status, "event_id": event_id})

        if self.path == "/api/demo/gate":
            try:
                confidence = float(data.get("confidence"))
            except (TypeError, ValueError):
                return self.json(400, {"status": "error", "error": "confidence must be number 0..1"})
            risk = str(data.get("risk", "")).lower()
            if not 0 <= confidence <= 1 or risk not in {"low", "medium", "high"}:
                return self.json(400, {"status": "error", "error": "invalid confidence or risk"})
            decision = "auto_execute" if confidence >= 0.85 and risk == "low" else "human_review"
            return self.json(200, {
                "status": "evaluated",
                "confidence": confidence,
                "risk": risk,
                "decision": decision,
                "rule": "auto_execute only when confidence>=0.85 and risk=low",
            })

        return self.json(404, {"status": "not_found"})

if __name__ == "__main__":
    init_db()
    ThreadingHTTPServer(("127.0.0.1", 8089), H).serve_forever()
